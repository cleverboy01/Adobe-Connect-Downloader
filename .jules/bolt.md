## 2024-05-23 - Avoid Small Chunked Reads for File Hashing
**Learning:** Using many small chunked reads (e.g., 64 reads of 4KB) for file hashing introduces significant I/O system call overhead.
**Action:** Use a single `read()` operation when extracting a fixed-size header. When optimizing this, do not hardcode the total computed byte size; instead, dynamically calculate it using the existing configuration variable (e.g., `self.config.video_hash_chunk_size * 64`) to preserve configuration flexibility.
