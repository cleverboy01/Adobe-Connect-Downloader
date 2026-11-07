## 2025-02-18 - File Hashing IO Overhead
**Learning:** The video hashing function was using many small chunked reads in a loop (`64 * 4096 bytes`), which introduces significant I/O system call overhead.
**Action:** Replace the looped small reads with a single dynamically sized `read()` operation (`self.config.video_hash_chunk_size * 64`) to minimize system calls and improve performance while preserving flexibility.
