


# Python OOP: Inheritance, Classes, and Magic Methods

This project covers fundamental concepts of object-oriented programming (OOP) in Python, including inheritance, classes, and magic methods.

---

## 📚 General Concepts

### 1️⃣ What is a superclass, base class, or parent class?

A **superclass** (also called a base class or parent class) is the class from which another class inherits. It defines common attributes and methods that can be reused by subclasses.

---

### 2️⃣ What is a subclass?

A **subclass** is a class that inherits from a superclass. It can reuse or override the functionality of the superclass and add its own attributes and methods.

---

### 3️⃣ How to list all attributes and methods of a class or instance?

Use the built-in `dir()` function:
```python
dir(MyClass)
dir(my_instance)
```

### 4️⃣ When can an instance have new attributes?

An instance can have new attributes anytime after it is created, by directly assigning them:

```python
obj.new_attr = "I am new!"
```

---

### 5️⃣ How to inherit a class from another?

Use parentheses after the class name:

```python
class ChildClass(ParentClass):
    pass
```

---

### 6️⃣ How to define a class with multiple base classes?

Separate the base classes by commas:

```python
class ChildClass(Parent1, Parent2):
    pass
```

---

### 7️⃣ What is the default class every class inherits from?

By default, every class in Python inherits from the built-in `object` class.

---

### 8️⃣ How to override a method or attribute inherited from the base class?

Redefine the method or attribute in the child class:

```python
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        print("Hello from Child")
```

---

### 9️⃣ Which attributes or methods are available by heritage to subclasses?

Subclasses inherit:

* All **public** and **protected** attributes and methods from the superclass.
* Private attributes and methods (prefixed with double underscores `__`) are name-mangled and not directly accessible by subclasses.

---

### 🔟 What is the purpose of inheritance?

Inheritance allows:

* Code reuse (avoiding repetition)
* Creating a logical hierarchy of classes
* Extending or customizing behavior in subclasses

---

## 🧭 Built-in Functions for Class and Type Checking

### `isinstance(object, classinfo)`

Check if an object is an instance of a specific class or its subclasses:

```python
isinstance(5, int)  # True
```

---

### `issubclass(class, classinfo)`

Check if a class is a subclass of another:

```python
issubclass(bool, int)  # True
```

---

### `type(object)`

Get the class type of an object:

```python
type(5)  # <class 'int'>
```

---

### `super()`

Call a method from the parent class:

```python
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()
        print("Hello from Child")
```

---

## 📌 Documentation

All modules, classes, and functions should include documentation (docstrings) explaining their purpose:

```python
"""
This module demonstrates inheritance in Python.
"""

class Animal:
    """
    Represents a generic animal.
    """
    def make_sound(self):
        """
        Returns a generic animal sound.
        """
        return "Some sound"
```

A documentation string is a **real sentence** explaining what the module, class, or method does.

---

✅ This README follows all project requirements (Ubuntu 20.04, Python 3.8.5, `pycodestyle` 2.7.x, and executable files).

✅ All code files must use `#!/usr/bin/python3` as the shebang and end with a newline.

✅ All test files must be `.txt` files inside the `tests` folder and executable with `python3 -m doctest ./tests/*`.

---
