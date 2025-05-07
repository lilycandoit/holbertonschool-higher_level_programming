# Import and Modules

## Description

This project explores Python modules and the import system, teaching you how to:

* Import functions and variables from other files
* Use imported functions effectively
* Create and structure your own modules
* Control code execution with the `if __name__ == "__main__"` guard
* Utilize the built-in `dir()` function for introspection
* Handle command-line arguments in Python scripts

## Learning Objectives

At the end of this project, you should be able to explain to anyone, without the help of Google:

* Why Python programming is awesome
* How to import functions from another file
* How to use imported functions
* How to create a module
* How to use the built-in function `dir()`
* How to prevent code in your script from being executed when imported
* How to use command-line arguments with your Python programs

## Requirements

Before you begin, ensure that:

* You are using one of the following editors: `vi`, `vim`, or `emacs`.
* Your files will be interpreted/compiled on Ubuntu 22.04 LTS using `python3` (version 3.10.\*).
* Every file ends with a newline character.
* The first line of each file is exactly:

  ```bash
  #!/usr/bin/python3
  ```
* This `README.md` file is present at the root of the project folder.
* Your code follows the `pycodestyle` (version 2.7.\*) style guide.
* All files are executable (`chmod +x`).
* The length of your files will be tested using `wc`, so keep them concise.

## Usage

1. Clone this repository:

   ```bash
   git clone <repository_url>
   cd import_and_modules
   ```
2. Make your scripts executable:

   ```bash
   chmod +x *.py
   ```
3. Run the main script:

   ```bash
   ./main.py
   ```
4. Inspect modules interactively:

   ```bash
   python3
   >>> import your_module
   >>> dir(your_module)
   ```

