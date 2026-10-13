## 2024-10-13 - Dynamic sizing for terminal progress bars
**Learning:** Fixed-width progress bars (like `ncols=80`) often cause terminal truncation or wrapping issues on smaller windows, degrading the CLI user experience.
**Action:** Always use `dynamic_ncols=True` and a clear `colour` (like 'green') when initializing `tqdm` to ensure the bar responsively adapts to the user's terminal window.
