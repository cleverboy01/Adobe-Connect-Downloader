## 2024-09-11 - CLI Argument Consistency
**Learning:** CLI arguments described in help messages or documentation must be explicitly added to `argparse`. In this project, `args.file` was handled in the script's execution path but `-f/--file` was completely missing from the parser configuration, resulting in unrecognized argument errors that break user trust and experience.
**Action:** Always verify that every flag documented in `--help` actually corresponds to an `add_argument` call and isn't just assumed to exist.
