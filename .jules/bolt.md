## 2026-10-19 - File Hashing System Call Overhead
**Learning:** Reading file chunks in a loop for hashing (e.g., 64 reads of 4KB) introduces unnecessary system call overhead compared to reading the exact amount in a single operation.
**Action:** When extracting fixed-size headers for hashing, use a single `read(size)` operation rather than chunking, dynamically calculating the size based on existing config to maintain flexibility.
