## 2024-05-23 - Optimize File Hashing I/O
**Learning:** Many small chunked reads (e.g., 64 reads of 4KB) for file hashing introduce significant I/O system call overhead.
**Action:** Use a single `read()` operation when extracting a fixed-size header. When optimizing this, dynamically calculate the total read size using existing configuration variables (e.g., `self.config.video_hash_chunk_size * 64`) to preserve configuration flexibility instead of hardcoding the byte size.
