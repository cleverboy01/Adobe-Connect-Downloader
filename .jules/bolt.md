## 2024-05-20 - File Hashing I/O Overhead
**Learning:** Avoid many small chunked reads (e.g., 64 reads of 4KB) for file hashing as it introduces significant I/O system call overhead.
**Action:** Use a single `read()` operation when extracting a fixed-size header. Calculate the total byte size dynamically using existing config variables (e.g., `self.config.video_hash_chunk_size * 64`).
