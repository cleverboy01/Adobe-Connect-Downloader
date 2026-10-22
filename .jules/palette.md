## 2024-05-24 - Dynamic TQDM sizing
**Learning:** Hardcoded ncols=80 truncates progress bars on smaller terminals and leaves wasted space on larger ones.
**Action:** Use dynamic_ncols=True and colour='green' to ensure terminal width is respected and to improve visual clarity for UX.