
# 🧠 Python OOP – Summary Guide

## 🧱 1. Class vs Object (Instance)

- **Class**: Blueprint or template for creating objects.
- **Object** (or instance): An individual instantiation of a class.

```python
class Dog:
    def __init__(self, name):
        self.name = name

my_dog = Dog("Buddy")  # Object of class Dog
```

## 🎯 2. Attributes

### 🔹 Instance Attribute

```python
class Dog:
    def __init__(self, name):
        self.name = name  # instance attribute
```

### 🔹 Class Attribute

```python
class Dog:
    species = "Canine"  # class attribute
```

## 🔒 3. Public vs Private Attributes

```python
class Dog:
    def __init__(self, name):
        self.__name = name  # private attribute

d = Dog("Max")
print(d.__name)  # ❌ AttributeError
```

## 🛠 4. Methods: Types and Usage

### ✅ Instance Method
```python
def bark(self):
    print(f"{self.name} says woof")
```

### ✅ Class Method
```python
@classmethod
def from_string(cls, data):
    name = data.split("-")[0]
    return cls(name)
```

### ✅ Static Method
```python
@staticmethod
def dog_years(age):
    return age * 7
```

## 🔁 5. Special (Dunder) Methods

| Method      | Purpose                                    |
|-------------|--------------------------------------------|
| `__init__`  | Constructor                                |
| `__str__`   | User-friendly string for print             |
| `__repr__`  | Developer string (for eval)                |
| `__del__`   | Destructor when object is deleted          |
| `__eq__` etc.| Comparison operators                      |

## 📤 6. Property, Getter & Setter

```python
class Rectangle:
    def __init__(self, width):
        self.__width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value
```

## 🧮 7. Class vs Instance Tracking

```python
class Rectangle:
    number_of_instances = 0

    def __init__(self):
        Rectangle.number_of_instances += 1

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
```

## 🧪 8. Eval and `__repr__`

```python
def __repr__(self):
    return f"Rectangle({self.width}, {self.height})"

new_rect = eval(repr(old_rect))
```

## 🎁 9. Factory Pattern with Classmethod

```python
@classmethod
def square(cls, size=0):
    return cls(size, size)
```

## 🧰 10. Static Utility Comparison

```python
@staticmethod
def bigger_or_equal(rect1, rect2):
    if rect1.area() >= rect2.area():
        return rect1
    return rect2
```

## 🧩 11. Other Common OOP Concepts

| Concept         | Description                              |
|----------------|------------------------------------------|
| Encapsulation   | Restricting direct access to data        |
| Abstraction     | Hiding complex logic behind interfaces   |
| Inheritance     | Deriving a class from another class      |
| Polymorphism    | Unified interface, different behaviors   |

## 🔚 Final Tips

- Use `@property` for attribute control.
- Use `@staticmethod` for helpers.
- Use `@classmethod` for alt constructors.
- Use `__str__` for print, `__repr__` for debug.

---

