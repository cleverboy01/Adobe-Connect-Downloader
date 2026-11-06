## 2024-05-15 - Dynamic Progress Bar UX
**Learning:** Hardcoding progress bar widths (e.g., ncols=80) can cause terminal output truncation. Using `dynamic_ncols=True` and a `colour` parameter improves the CLI user experience across different terminal sizes.
**Action:** Use `dynamic_ncols=True` and `colour='green'` when initializing tqdm progress bars.
