## 2024-05-15 - I/O Overhead in File Hashing
**Learning:** Performing many small chunked reads (e.g., 64 iterations of 4KB reads) for file hashing introduces significant I/O system call overhead.
**Action:** Use a single `read()` operation when extracting a fixed-size header, dynamically calculating total read size (e.g., `chunk_size * 64`) to preserve flexibility while optimizing I/O.
