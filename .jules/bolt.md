## 2024-05-16 - File Hashing I/O Overhead
**Learning:** Avoid many small chunked reads (e.g., 64 reads of 4KB) for file hashing, as it introduces significant I/O system call overhead.
**Action:** Replace looped small chunk reads with a single dynamically calculated block read (`chunk_size * N`) to reduce I/O overhead while preserving configuration flexibility.