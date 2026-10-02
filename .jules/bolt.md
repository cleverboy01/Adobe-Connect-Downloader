## 2024-05-24 - Optimize file hashing chunk size
**Learning:** Avoid many small chunked reads (e.g., 64 reads of 4KB) for file hashing, as it introduces significant I/O system call overhead.
**Action:** Use a single, properly sized read() operation when extracting a fixed-size header (e.g., ~256KB) for hashing or validation.