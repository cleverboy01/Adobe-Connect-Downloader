## 2024-10-04 - Optimize file hashing I/O overhead
**Learning:** Avoid many small chunked reads (e.g., 64 reads of 4KB) for file hashing, as it introduces significant I/O system call overhead.
**Action:** Instead, use a single, properly sized `read()` operation when extracting a fixed-size header (e.g., ~256KB) for hashing or validation.
