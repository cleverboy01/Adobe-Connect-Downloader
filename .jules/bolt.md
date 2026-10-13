## 2024-10-24 - File Hashing I/O Bottleneck
**Learning:** Performing many small chunked reads (e.g., 64 reads of 4KB) for file hashing introduces significant I/O system call overhead.
**Action:** Use a single `read()` operation when extracting a fixed-size header. Dynamically calculate the total byte size using existing configuration variables instead of hardcoding it to preserve flexibility.
