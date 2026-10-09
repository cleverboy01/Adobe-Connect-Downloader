## 2024-10-24 - Avoid excessive I/O system calls
**Learning:** Repeated small chunked reads (e.g. 64 reads of 4KB) for file hashing introduce significant I/O system call overhead compared to a single read.
**Action:** Use a single read operation when extracting a fixed-size header. Dynamically calculate the total bytes needed rather than hardcoding to preserve configuration flexibility.
