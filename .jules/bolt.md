## 2024-05-15 - [File Hashing I/O Overhead]
**Learning:** Looping small file reads (`f.read(chunk_size)`) to hash part of a file introduces unnecessary I/O system call overhead compared to a single larger read (`f.read(chunk_size * iterations)`).
**Action:** Always prefer reading the total required byte size in a single `read()` operation when hashing a fixed portion of a file, calculating the size dynamically from config to maintain flexibility.
