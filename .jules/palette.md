## 2024-09-16 - CLI Feature Advertisement Without Implementation
**Learning:** The CLI help text advertised a batch feature (`-f` / `--file`), and the code had logic to handle `args.file`, but the argument itself was never registered in `argparse`. This creates a confusing UX where users are told they can do something but the tool rejects the command.
**Action:** When adding conditional logic for a CLI argument or documenting a feature in the help text, always ensure the corresponding `add_argument` call exists in the parser setup.
