## 2024-05-24 - Progress Bar UX and Terminal Truncation
**Learning:** Hardcoding `ncols=80` or omitting width configurations for `tqdm` progress bars can cause terminal output truncation and poor visual clarity on different screen sizes. A reusable UX pattern for this codebase is to use `dynamic_ncols=True` and a `colour` parameter (e.g., 'green').
**Action:** Always use `dynamic_ncols=True, colour='green'` when initializing `tqdm` progress bars to ensure responsiveness and improved visibility.
