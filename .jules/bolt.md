## 2024-10-01 - I/O Optimization
**Learning:** Avoid small chunked reads for hashing (e.g., 64 reads of 4KB), as it introduces significant I/O system call overhead.
**Action:** Use a single, properly sized read() operation when extracting a fixed-size header for hashing.
