## 2024-05-15 - [File Hashing Optimization]
**Learning:** Multiple small `read()` operations (e.g., 64 reads of 4KB) for file hashing introduce significant I/O system call overhead compared to a single larger `read()`.
**Action:** When extracting fixed-size headers for hashing, compute the total size dynamically from configuration and use a single `read()` call to minimize context switching overhead.
