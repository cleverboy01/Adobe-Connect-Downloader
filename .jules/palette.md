## 2024-05-24 - Dynamic Progress Bars in CLI
**Learning:** Hardcoding column width for CLI progress bars can lead to text truncation on smaller terminal windows, degrading the UX. Using dynamic_ncols combined with color helps the progress bar adapt properly and provides clearer visual feedback.
**Action:** Always prefer `dynamic_ncols=True` and add a `colour` parameter (e.g., 'green') when initializing `tqdm` progress bars in CLI applications.
