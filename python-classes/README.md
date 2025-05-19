# Python - Classes and Objects

## Description

This project is part of the Holberton School curriculum, focusing on the principles of Object-Oriented Programming (OOP) in Python. It introduces how to define and use classes, objects, attributes, methods, and special methods like `__init__`, `__str__`, and `__repr__`. The project also reinforces concepts like data encapsulation, abstraction, and the proper use of documentation and coding style.

## Requirements

- All code is written in Python 3.8.5
- Interpreted on Ubuntu 20.04 LTS
- Files must end with a new line
- Files start with: `#!/usr/bin/python3`
- Code style follows: `pycodestyle`
- All files must be executable
- All modules, classes, and functions include proper docstrings
- Each file length will be tested using the `wc` command

## Project Structure

- Each Python file contains one or more class definitions or object manipulations
- Classes demonstrate use of:
  - Instance and class attributes
  - Public and private attributes
  - Getters and setters
  - Properties using `@property`
  - Method overriding and inheritance
  - Special methods like `__str__`, `__repr__`, and `__init__`

## Usage

To test a specific file or print documentation:

```bash
python3 -c 'print(__import__("my_module").__doc__)'
python3 -c 'print(__import__("my_module").MyClass.__doc__)'
python3 -c 'print(__import__("my_module").my_function.__doc__)'
python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
```