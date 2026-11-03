## 2024-05-24 - File Hashing I/O Overhead
**Learning:** Many small chunked reads introduce significant I/O system call overhead when hashing files.
**Action:** Use a single `read()` operation when extracting a fixed-size header, dynamically calculating the total read size using configuration variables rather than hardcoding byte counts to preserve flexibility.
