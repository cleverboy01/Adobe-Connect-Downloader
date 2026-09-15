## 2024-05-24 - CLI Argparse UX Clarity
**Learning:** Using `metavar` in `argparse` drastically improves the readability of generated help output, and it's critical to ensure all arguments advertised in documentation or epilogs (like `--file` for batch processing) are actually registered in the parser to avoid confusing users.
**Action:** Always verify that documented features map directly to `argparse` options, and use `metavar` to provide clear, semantic names for argument values in the CLI help text.
