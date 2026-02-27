# 🎥 Adobe Connect Downloader: How to Download Adobe Connect Recordings to MP4

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![FFmpeg Required](https://img.shields.io/badge/FFmpeg-Required-orange.svg)](https://ffmpeg.org/)
[![SEO Optimized](https://img.shields.io/badge/SEO-Optimized-brightgreen.svg)](#)

**Adobe Connect Downloader** is the ultimate tool to **download Adobe Connect recordings** and convert them into high-quality **MP4** files. Designed for students, educators, and professionals, this script provides a seamless way to **save Adobe Connect meetings offline** for later viewing, even without an active internet connection.

Whether you need to **export Adobe Connect recordings**, **convert FLV to MP4**, or simply keep a local archive of your webinars, this tool offers professional-grade features with zero manual setup.

---

## 🔥 Key Features for Adobe Connect Recording Download

- **Download Adobe Connect Recording to MP4**: Automatically merges separate audio and video streams into a single, high-definition MP4 file.
- **Hardware Accelerated Encoding**: Uses your GPU (**NVIDIA NVENC**, **Intel/AMD VAAPI**) for lightning-fast processing—save hours on long lectures.
- **Smart A/V Synchronization**: Fixes common sync issues automatically, ensuring your **Adobe Connect offline video** is perfectly aligned.
- **Batch Adobe Connect Download**: Process multiple URLs at once using a simple CSV list—ideal for entire semesters of classes.
- **Secure Authentication Handling**: Supports browser session cookies to **download private Adobe Connect recordings** securely.
- **Zero-Dependency Bootstrapper**: Automatically creates a virtual environment and installs everything you need.

---

## 🛠️ Prerequisites & Setup

To use this **Adobe Connect download tool**, you only need two things:

1. **Python 3.8+**: [Download Python from the official site](https://www.python.org/downloads/).
2. **FFmpeg**: Essential for merging media streams.

### How to Install FFmpeg for Adobe Connect Downloader:

- **Windows**: Download from [gyan.dev](https://www.gyan.dev/ffmpeg/builds/), extract, and add the `bin` folder to your System PATH.
- **macOS**: Run `brew install ffmpeg`.
- **Linux**: Run `sudo apt install ffmpeg`.

*Verify by running `ffmpeg -version` in your terminal.*

---

## 📖 How to Download Adobe Connect Recordings (Usage Guide)

### 1. Simple Single URL Download
To **save an Adobe Connect recording**, run:
```powershell
python adobe_downloader.py "https://your-university.adobeconnect.com/p12345678/"
```

### 2. Custom Filename
Give your **Adobe Connect video** a specific name:
```powershell
python adobe_downloader.py "URL" -o "Marketing_Lecture_01.mp4"
```

### 3. Batch Download (Multiple Recordings)
Create a `list.csv` file with your **Adobe Connect links**:
```csv
https://example.com/p123/,Introduction
https://example.com/p456/,Advanced_Topic
```
Then execute:
```powershell
python adobe_downloader.py --file list.csv
```

### 4. Download Restricted/Private Recordings
If your recording requires a login, use your browser's session cookie:
1. Log in to the room in your browser.
2. In **Developer Tools (F12)** -> **Network**, find the `BREEZESESSION` cookie.
3. Run with the `--cookies` flag:
```powershell
python adobe_downloader.py "URL" --cookies "BREEZESESSION=your_value"
```

---

## ❓ Frequently Asked Questions (FAQ)

### How can I watch Adobe Connect recordings offline?
By using this **Adobe Connect Downloader**, you can convert the online stream into an MP4 file, allowing you to watch your classes on any device (phone, tablet, PC) without needing an internet connection.

### Is there a free Adobe Connect downloader?
Yes, this project is completely open-source and free to use. It provides a more reliable alternative to screen recording.

### Can I convert Adobe Connect FLV to MP4?
Yes, the script automatically handles the extraction of FLV files and uses FFmpeg to mux them into a standard MP4 format.

### Why does my download show "HTML instead of ZIP"?
This usually means the recording is private. Follow the **Authenticated Downloads** section above to fix this using cookies.

---

## ⚙️ Technical Overview
This tool automates the complex process of fetching raw Adobe Connect assets. It identifies the unique **SCO-ID**, downloads the assets, probes for hardware encoders, and merges everything into a portable format.
