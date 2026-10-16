## 2024-05-24 - File Hashing Overhead
**Learning:** Many small chunked reads (e.g., 64 reads of 4KB) for file hashing introduce significant I/O system call overhead, which acts as a bottleneck.
**Action:** Use a single `read()` operation when extracting a fixed-size header, and dynamically calculate the total byte size using configuration variables (e.g., `config.video_hash_chunk_size * 64`) to preserve flexibility.
