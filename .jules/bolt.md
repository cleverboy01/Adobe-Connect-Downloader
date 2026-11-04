## 2024-05-24 - File Hashing I/O Overhead
**Learning:** Avoid many small chunked reads for file hashing, as it introduces significant I/O system call overhead compared to a single larger read.
**Action:** Use a single `read()` operation when extracting a fixed-size header, dynamically calculating the total read size using configuration variables (e.g., `self.config.video_hash_chunk_size * 64`) rather than hardcoding byte counts to preserve flexibility.
