## 2026-09-30 - Optimize file hashing I/O
**Learning:** Using many small chunked reads (e.g., 64 reads of 4KB) for file hashing introduces significant I/O system call overhead.
**Action:** Use a single, properly sized `read()` operation when extracting a fixed-size header (e.g., ~256KB) for hashing or validation.
