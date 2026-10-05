## 2024-05-24 - File Hashing I/O Overhead
**Learning:** Performing many small chunked reads (e.g., 64 reads of 4KB) for file hashing introduces significant I/O system call overhead compared to reading a larger chunk all at once.
**Action:** Use a single `read()` operation when extracting a fixed-size header. Avoid hardcoding total byte size; dynamically calculate it using configuration variables (e.g. `config.video_hash_chunk_size * 64`).
