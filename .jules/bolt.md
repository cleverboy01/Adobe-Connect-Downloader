## 2024-10-25 - File Hashing I/O Anti-pattern
**Learning:** The codebase previously used many small chunked reads (`f.read(4096)` in a loop) for file hashing, which introduces significant I/O system call overhead in Python.
**Action:** When extracting a fixed-size header for hashing, use a single `read()` operation dynamically calculating the total size (e.g., `f.read(config.chunk_size * 64)`) to minimize system calls while remaining flexible.
