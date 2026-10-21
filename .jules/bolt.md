## 2024-05-15 - Optimizing File Hashing I/O Overhead
**Learning:** Many small chunked reads (e.g., 64 reads of 4KB) for file hashing introduce significant I/O system call overhead in Python.
**Action:** Use a single `read()` operation when extracting a fixed-size header dynamically calculated from config to preserve flexibility while improving performance.
