
# 📘 Python - Input/Output

## 📝 Description

This project is part of the **Holberton School Higher Level Programming** curriculum.
It focuses on how to perform file input/output (I/O) operations in Python, including reading from and writing to files, working with JSON data, and accessing command line arguments.

---

## 🎯 Learning Objectives & Review Notes

### ✅ Why Python programming is awesome
- Simple syntax, readable code
- Supports multiple programming paradigms
- Huge standard library and active community
- Cross-platform and widely used in real-world applications

---

### ✅ How to open a file
```python
file = open("file.txt", "r")  # Modes: 'r' = read, 'w' = write, 'a' = append
````

---

### ✅ How to write text in a file

```python
with open("file.txt", "w") as file:
    file.write("Hello, world!")
```

---

### ✅ How to read the full content of a file

```python
with open("file.txt", "r") as file:
    content = file.read()
    print(content)
```

---

### ✅ How to read a file line by line

```python
with open("file.txt", "r") as file:
    for line in file:
        print(line.strip())
```

---

### ✅ How to move the cursor in a file

```python
file.seek(0)     # Move to beginning
position = file.tell()  # Get current position
```

---

### ✅ How to make sure a file is closed after using it

Use the `with` statement:

```python
with open("file.txt", "r") as file:
    data = file.read()
# File is automatically closed here
```

---

### ✅ What is and how to use the `with` statement

A context manager that ensures resources (like files) are properly cleaned up:

```python
with open("file.txt", "r") as file:
    print(file.read())
```

---

### ✅ What is JSON

* Stands for **JavaScript Object Notation**
* Text format for structured data exchange
* Python supports it using the `json` module

---

### ✅ What is serialization

* Turning a Python object (e.g., dict, list) into a string or byte stream
* Used for saving or transmitting data (e.g., with JSON)

---

### ✅ What is deserialization

* Turning a serialized string (like JSON) back into a Python object

---

### ✅ How to convert a Python data structure to a JSON string

```python
import json
data = {"name": "Alice", "age": 25}
json_string = json.dumps(data)
```

---

### ✅ How to convert a JSON string to a Python data structure

```python
import json
json_string = '{"name": "Alice", "age": 25}'
data = json.loads(json_string)
```

---

### ✅ How to access command line parameters in a Python script

```python
import sys
print(sys.argv)  # argv[0] is the script name; argv[1:] are the arguments
```

---

## 🧪 Testing & Documentation

* All modules and functions must include full docstrings
* Test files should go in a `tests/` directory and use `.txt` extension
* Use `doctest` to validate:

```bash
python3 -m doctest ./tests/*
```

