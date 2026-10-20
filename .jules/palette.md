## 2024-10-20 - Initial setup
**Learning:** Started tracking UX/a11y insights.
**Action:** Track UX patterns in this repo.

## 2024-10-20 - CLI Progress Bar UX
**Learning:** Fixed-width terminal progress bars can truncate outputs; lacking colors reduces visual clarity in CLI apps.
**Action:** Always use `dynamic_ncols=True` and `colour='green'` for tqdm progress bars to prevent truncation and improve visual UX in command-line tools.
