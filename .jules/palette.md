## 2024-05-20 - [CLI UX Fix: Exposed batch `--file` Argument]
**Learning:** The application possessed latent logic for processing a batch of URLs from a CSV file (e.g., `list.csv`), referenced explicitly in the epilog of the `argparse` configuration. However, the required `-f` / `--file` argument was entirely missing from the parser configuration itself. Adding this missing argument unblocked the latent batch functionality.
**Action:** Always verify that arguments described in tool epilogs or documentation are actually exposed as available arguments via the parsing library (e.g., `argparse`).
