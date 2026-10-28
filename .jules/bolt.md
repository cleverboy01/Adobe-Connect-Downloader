## 2024-05-20 - [File Hashing I/O Optimization]
**Learning:** Using many small chunked reads for file hashing introduces significant I/O system call overhead.
**Action:** Use a single `read()` operation when extracting a fixed-size header, dynamically calculating the total read size using configuration variables (e.g., `self.config.video_hash_chunk_size * 64`) rather than hardcoding byte counts to preserve flexibility.
