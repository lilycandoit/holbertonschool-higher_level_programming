# Python - Hello, World

This project is a warm-up introduction to Python programming. It covers basic syntax, scripting, formatting, and best practices, using the Python 3.8 environment on Ubuntu 20.04 LTS.

## Learning Objectives

By the end of this project, you should be able to:

- Write and run Python scripts from the command line.
- Understand and use the `print()` function.
- Use shebang (`#!/usr/bin/python3`) to make scripts executable.
- Apply basic string formatting with `f-strings`.
- Work with string slicing and concatenation.
- Understand and follow Python style guidelines (PEP8 with `pycodestyle`).
- Use hidden Python modules like `this` (Zen of Python).
- Use the Unix commands `chmod`, `wc`, and `pycodestyle`.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- Python version: 3.8.*
- Code must be executable and start with `#!/usr/bin/python3`
- All files end with a new line
- Follow `pycodestyle` (version 2.7.*)
- No unnecessary string casting
- No loops or conditionals unless allowed
- Line length must not exceed 79 characters

## Usage

Make scripts executable:
```bash
chmod +x *.py
```

Run a script:
```bash
./2-print.py
```

Check line count:
```bash
wc -l 2-print.py
```

Validate style:
```bash
pycodestyle 2-print.py
```

