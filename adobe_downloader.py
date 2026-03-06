#!filepath: adobe_downloader.py
# --- Step 0: Bootstrap Environment ---
import bootstrap
bootstrap.bootstrap()

# --- Step 1: Standard Library Imports ---
import os
import re
import sys
import shutil
import zipfile
import argparse
import logging
import csv
from urllib.parse import urlparse
from collections import defaultdict
from typing import List, Tuple, Optional, Dict

# --- Step 2: Local Module Imports ---
# Moved imports inside functions that use them to align with the new structure

# --- Main Processing Function for a Single URL ---
def process_single_url(url: str, custom_filename: Optional[str], file_ops, ffmpeg_handler, quality):
    """
    Handles the entire download and processing for a single Adobe Connect URL.
    This function contains the core logic of the downloader application.
    """
    from progress_display import TqdmProgress
    from ffmpeg_handler import NormalizedMedia

    logging.info(f"--- Processing URL: {url} ---")
    
    # Initialize session with optional cookies
    session = setup_session(getattr(file_ops, 'cookies', None))
    
    recording_id, id_type = get_id_and_type(url, session)
    if not recording_id:
        logging.error(f"Could not get a valid recording ID for {url}. Skipping.")
        return False

    safe_recording_id = file_ops.safe_filename(recording_id)
    main_download_dir = file_ops.get_main_download_dir()
    
    # Create a temporary subdirectory for this specific download
    temp_output_dir = os.path.join(main_download_dir, f"adobe_connect_{safe_recording_id}")
    os.makedirs(temp_output_dir, exist_ok=True)
    zip_path = os.path.join(temp_output_dir, f"{safe_recording_id}.zip")

    # Determine the final output filename
    output_filename = custom_filename if custom_filename else f"recording_{safe_recording_id}.mp4"
    if not output_filename.lower().endswith('.mp4'):
        output_filename += '.mp4'
    
    # The final video will first be created inside the temp dir
    final_video_path_temp = os.path.join(temp_output_dir, file_ops.safe_filename(output_filename))
    
    # The final destination for the video is one level up
    final_video_path_dest = os.path.join(main_download_dir, file_ops.safe_filename(output_filename))
    
    logging.info(f"Final video will be named: '{output_filename}'")
    
    if os.path.exists(final_video_path_dest):
        logging.warning(f"Output file '{output_filename}' already exists in the destination. Skipping.")
        cleanup_temp_directory(temp_output_dir)
        return True

    # --- Download and Extract ---
    if not os.path.exists(zip_path):
        zip_urls = construct_zip_urls(url, recording_id, id_type, session)
        success = False
        for zip_url in zip_urls:
            logging.info(f"Trying download from: {zip_url}")
            if download_zip_file(zip_url, zip_path, TqdmProgress, session):
                success = True
                break
        
        if not success:
            cleanup_temp_directory(temp_output_dir)
            return False
            
        logging.info(f"Extracting '{os.path.basename(zip_path)}'...")
        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(temp_output_dir)
        except zipfile.BadZipFile:
            logging.critical("Downloaded file is not a valid zip archive.")
            cleanup_temp_directory(temp_output_dir)
            return False
    else:
        logging.warning("ZIP file already exists. Skipping download and extraction.")

    # --- Two-Pass Workflow ---
    media_streams = find_media_streams(temp_output_dir)
    if 'screenshare' not in media_streams:
        logging.critical("CRITICAL: 'screenshare' stream is missing. Cannot proceed.")
        cleanup_temp_directory(temp_output_dir)
        return False

    # --- FIX: Call the NormalizedMedia class directly ---
    normalized_media = NormalizedMedia(
        video_path=os.path.join(temp_output_dir, "normalized_video.mkv"),
        audio_path=os.path.join(temp_output_dir, "normalized_audio.m4a")
    )

    # Pass 1.1: Normalize Video Stream
    video_files = media_streams.get('screenshare')
    if not ffmpeg_handler.normalize_video_stream(video_files, normalized_media.video_path, quality):
        logging.critical("❌ Failed during video normalization pass.")
        cleanup_temp_directory(temp_output_dir)
        return False

    # Pass 1.2: Normalize Audio Stream
    audio_files = media_streams.get('cameravoip', media_streams.get('screenshare'))
    if not ffmpeg_handler.normalize_audio_stream(audio_files, normalized_media.audio_path):
        logging.critical("❌ Failed during audio normalization pass.")
        cleanup_temp_directory(temp_output_dir)
        return False

    # Pass 2: Final Merge
    if ffmpeg_handler.merge_normalized_streams(normalized_media, final_video_path_temp, quality):
        # --- Final file move and cleanup ---
        logging.info(f"Moving final video to main download directory...")
        shutil.move(final_video_path_temp, final_video_path_dest)
        logging.info(f"✅ Success! Video saved to: {os.path.abspath(final_video_path_dest)}")
        cleanup_temp_directory(temp_output_dir)
        return True
    else:
        logging.critical("❌ Failed to create the final video file after all attempts.")
        cleanup_temp_directory(temp_output_dir)
        return False

# --- Main Application Controller ---
def main():
    """
    Main entry point. Parses arguments and controls whether to process a single
    URL or a batch file of URLs.
    """
    from file_operations import CrossPlatformFileOps
    from ffmpeg_handler import FFmpegHandler
    from detector.config import QualityProfile

    logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"), format='%(asctime)s - [%(levelname)s] - %(message)s', datefmt='%H:%M:%S')
    
    parser = argparse.ArgumentParser(
        description="Adobe Connect Downloader - Universal Edition (v17.0 - Batch Mode)",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="This universal version automatically detects and uses the best available GPU.\n"
               "It can process a single URL or a batch file (e.g., list.csv).\n"
               "Example batch file format:\n"
               "https://my.adobeconnect.com/p123/,My First Lecture\n"
               "https://my.adobeconnect.com/p456/,My Second Lecture.mp4\n"
               "https://my.adobeconnect.com/p789/,(no filename, uses default)"
    )
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("url", nargs='?', default=None, help="The single Adobe Connect recording URL to download.")
    parser.add_argument("-o", "--output", help="Optional output filename (only used with single URL).")
    parser.add_argument("--cookies", help="Authentication cookies (string or path to cookies.txt).")
    parser.add_argument("--quality", choices=[q.value for q in QualityProfile], default='medium', help="Encoding quality preset.")
    
    args = parser.parse_args()

    logging.info(f"--- Adobe Downloader v17.0 (Batch Mode Edition) ---")
    quality = QualityProfile(args.quality)
    file_ops = CrossPlatformFileOps()
    file_ops.cookies = args.cookies
    
    try:
        ffmpeg_handler = FFmpegHandler()
    except FileNotFoundError as e:
        logging.critical(f"FATAL ERROR: {e}")
        logging.critical("Please ensure FFmpeg is installed and accessible in your system's PATH.")
        sys.exit(1)

    if args.url:
        # Single URL mode
        process_single_url(args.url, args.output, file_ops, ffmpeg_handler, quality)
    elif args.file:
        # Batch file mode
        try:
            with open(args.file, 'r', encoding='utf-8') as f:
                # Read all lines to get a total count for progress logging
                lines = list(csv.reader(f))
                total_links = len(lines)
                logging.info(f"Found {total_links} links in '{args.file}'. Starting batch download.")

                for i, row in enumerate(lines):
                    if not row or not row[0].strip():
                        continue # Skip empty lines

                    link = row[0].strip()
                    # Filename is optional (column 2)
                    filename = row[1].strip() if len(row) > 1 and row[1].strip() else None
                    
                    print("-" * 60)
                    logging.info(f"Processing link {i+1} of {total_links}...")
                    
                    process_single_url(link, filename, file_ops, ffmpeg_handler, quality)
                
                logging.info("Batch processing complete.")

        except FileNotFoundError:
            logging.critical(f"Error: The specified file was not found: {args.file}")
            sys.exit(1)
        except Exception as e:
            logging.critical(f"An unexpected error occurred while reading the file: {e}")
            sys.exit(1)

# --- All Helper Functions ---
def setup_session(cookie_str: Optional[str]) -> 'requests.Session':
    import requests
    session = requests.Session()
    session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})
    
    if cookie_str:
        if os.path.exists(cookie_str):
            with open(cookie_str, 'r') as f:
                cookie_str = f.read().strip()
        
        domain = 'my.adobeconnect.com' # Default to standard domain
        for cookie in cookie_str.split(';'):
            if '=' in cookie:
                name, value = cookie.strip().split('=', 1)
                session.cookies.set(name.strip(), value.strip(), domain=domain)
    return session

def get_id_and_type(meeting_url: str, session: 'requests.Session') -> Optional[Tuple[str, str]]:
    import requests
    logging.info(f"Analyzing URL: {meeting_url}")
    try:
        response = session.get(meeting_url, timeout=15)
        response.raise_for_status()
        
        # More robust SCO-ID search
        patterns = [
            r'"sco-id"\s*:\s*"(\d+)"',
            r'sco-id=(\d+)',
            r'recording-id=(\d+)',
            r'scoid:(\d+)'
        ]
        for p in patterns:
            match = re.search(p, response.text, re.IGNORECASE)
            if match:
                found_id = match.group(1)
                logging.info(f"Found SCO-ID: {found_id}")
                return found_id, 'sco-id'
                
    except Exception as e:
        logging.warning(f"Initial analysis issue: {e}")
    
    # Fallback to path ID
    path_part = urlparse(meeting_url).path.strip('/')
    path_match = re.search(r'([a-zA-Z0-9_-]+)$', path_part.split('?')[0])
    if path_match:
        found_id = path_match.group(1)
        logging.info(f"Using Path ID: {found_id}")
        return found_id, 'path-id'
    
    return None, None

def get_account_id(meeting_url: str, session: 'requests.Session') -> Optional[str]:
    try:
        response = session.get(meeting_url, timeout=10)
        match = re.search(r'account_id\s*=\s*(\d+)', response.text)
        if match:
            return match.group(1)
    except:
        pass
    return None

def construct_zip_urls(meeting_url: str, recording_id: str, id_type: str, session: 'requests.Session') -> List[str]:
    parsed_url = urlparse(meeting_url)
    base = f"{parsed_url.scheme}://{parsed_url.netloc}"
    urls = []
    
    account_id = get_account_id(meeting_url, session)
    
    # Structure A: Using the ID directly (common in new versions)
    urls.append(f"{base}/{recording_id}/output/{recording_id}.zip?download=zip")
    urls.append(f"{base}/{recording_id}/output/output.zip?download=zip")
    
    # Structure B: Using 'p' prefix (common with SCO-IDs)
    urls.append(f"{base}/p{recording_id}/output/{recording_id}.zip?download=zip")
    urls.append(f"{base}/p{recording_id}/output/output.zip?download=zip")

    # Structure C: Content-based (Newer discovery)
    if account_id:
        urls.append(f"{base}/content/{account_id}/{recording_id}-1/output/{recording_id}-1.zip?download=zip")
        urls.append(f"{base}/content/{account_id}/{recording_id}-1/output/output.zip?download=zip")
    
    return list(dict.fromkeys(urls)) # Remove duplicates

def download_zip_file(zip_url: str, output_path: str, Progress_class, session: 'requests.Session') -> bool:
    try:
        with session.get(zip_url, stream=True, timeout=30) as r:
            if r.status_code != 200: return False
            content_type = r.headers.get('Content-Type', '').lower()
            if 'html' in content_type:
                logging.warning(f"Url returned HTML instead of ZIP. Likely login required or wrong link.")
                return False
            
            total_size = int(r.headers.get('content-length', 0))
            from progress_display import TqdmProgress
            progress2 = TqdmProgress(total_size, "Downloading ZIP")
            with open(output_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024*100):
                    f.write(chunk)
                    progress2.update(len(chunk))
            progress2.finish()
            return True
    except Exception as e:
        logging.error(f"Error downloading {zip_url}: {e}")
        return False

def find_media_streams(extract_folder: str) -> Dict[str, List[str]]:
    """Finds and sorts all media stream files (.flv) in the directory."""
    logging.info("Scanning directory for media streams...")
    streams = defaultdict(list)
    for filename in os.listdir(extract_folder):
        if filename.lower().endswith('.flv'):
            if match := re.match(r'([a-zA-Z0-9]+)_', filename):
                streams[match.group(1).lower()].append(os.path.join(extract_folder, filename))
    
    sort_key = lambda f: int(os.path.splitext(os.path.basename(f))[0].split('_')[-1]) if os.path.splitext(os.path.basename(f))[0].split('_')[-1].isdigit() else 0
    for stream_name in streams:
        streams[stream_name] = sorted(streams[stream_name], key=sort_key)
        
    if not streams.get('cameravoip'):
        logging.warning("No separate camera/audio stream found. Audio will be extracted from the screenshare stream.")
        
    return streams

def cleanup_temp_directory(dir_path: str) -> None:
    """Recursively removes the given temporary directory, ignoring errors."""
    logging.debug(f"Cleaning up temporary directory: {dir_path}")
    if os.path.isdir(dir_path):
        try:
            shutil.rmtree(dir_path)
            logging.debug(f"Removed temp directory: {dir_path}")
        except OSError as e:
            logging.warning(f"Could not clean up temp directory: {e}")

if __name__ == "__main__":
    main()
