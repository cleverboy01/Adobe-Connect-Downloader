## 2024-10-06 - Avoid small chunked reads for file hashing
**Learning:** Using many small chunked reads (e.g., 64 reads of 4KB) for file hashing introduces significant I/O system call overhead.
**Action:** Use a single `read()` operation with a dynamically calculated total size (e.g., `chunk_size * 64`) to minimize I/O overhead while preserving configuration flexibility.