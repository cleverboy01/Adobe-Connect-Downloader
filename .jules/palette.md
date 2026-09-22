## 2026-09-22 - Tqdm Terminal Progress Bar UX
**Learning:** Hardcoding `ncols` in `tqdm` progress bars can cause terminal truncation issues for users on different window sizes, degrading the CLI UX. Using `dynamic_ncols=True` ensures the bar adapts perfectly, and adding a `colour` parameter (e.g., 'green') improves visual clarity and gives clear feedback.
**Action:** Always use `dynamic_ncols=True` and `colour` parameters when initializing `tqdm` progress bars in CLI tools to ensure responsive and accessible terminal output.
