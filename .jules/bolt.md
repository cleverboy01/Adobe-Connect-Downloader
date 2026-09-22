## 2024-05-24 - Optimizing FFmpeg output parsing
**Learning:** Parsing continuous `stderr` stream from long-running FFmpeg processes can introduce significant CPU overhead if regular expressions are uncompiled and execute on every single line, many of which don't contain the targeted information (e.g., `time=...`).
**Action:** Always compile frequently used regex patterns in tight loops at the module level. Utilize fast-path string checks (e.g. `if "pattern" not in line`) before executing the more expensive regex match.
