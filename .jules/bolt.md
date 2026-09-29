## 2023-10-24 - File Hashing I/O Bottleneck
**Learning:** Performing many small chunked reads (e.g., 64 reads of 4KB) for file hashing introduces significant I/O system call overhead compared to a single larger read operation, even when the total data size is relatively small (~256KB).
**Action:** Replace chunked reading loops with a single, properly sized `read()` operation when extracting a fixed-size header for hashing or validation, significantly reducing overhead.
