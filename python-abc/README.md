
# Python OOP: Abstract Class, Interface, Duck Typing, Subclassing, and Mixins

This guide summarizes key concepts in Python Object-Oriented Programming (OOP), including abstract classes, interfaces, duck typing, subclassing base classes, method overriding, multiple inheritance, and mixins. Each section includes clear explanations and hands-on examples.

---

## 📌 1. Abstract Classes

### What is it?

An **abstract class** defines a **common interface** for a group of related classes but **cannot be instantiated directly**.

### Example:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r**2

    def perimeter(self):
        return 2 * 3.14 * self.r
```

---

## 📌 2. Interfaces and Duck Typing

### Interface in Python

Python doesn’t have explicit interfaces, but abstract classes can simulate them. An **interface** is a set of methods that a class must implement.

### Duck Typing

“If it looks like a duck and quacks like a duck, it’s a duck.”
✅ Python relies on **behavior, not type**.

### Example:

```python
class Bird:
    def fly(self):
        print("Flying...")

class Plane:
    def fly(self):
        print("Jetting through the sky!")

def takeoff(flyer):
    flyer.fly()

takeoff(Bird())
takeoff(Plane())
```

---

## 📌 3. Subclassing Standard Base Classes

### What is it?

You can **inherit** from built-in classes (like `list`, `dict`) and add your own behavior.

### Example:

```python
class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added {item} to the list")

v = VerboseList()
v.append(5)
```

---

## 📌 4. Method Overriding

### What is it?

When a **subclass provides its own implementation** of a method already defined in the parent class.

### Example:

```python
class Animal:
    def sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark!")

d = Dog()
d.sound()  # Bark!
```

---

## 📌 5. Multiple Inheritance

### What is it?

A class can inherit from **more than one parent class**.

### Example:

```python
class Flyer:
    def fly(self):
        print("I can fly")

class Swimmer:
    def swim(self):
        print("I can swim")

class Duck(Flyer, Swimmer):
    pass

d = Duck()
d.fly()
d.swim()
```

---

## 📌 6. Mixins

### What is it?

A **mixin** is a small class that provides additional behavior, meant to be used alongside other classes.

### Example:

```python
class LoggerMixin:
    def log(self, message):
        print(f"[LOG] {message}")

class Task(LoggerMixin):
    def run(self):
        self.log("Task is running")

t = Task()
t.run()
```

---

## 📌 Bonus: Iterator Example (CountedIterator)

### Example:

```python
class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        return self.count

data = [1, 2, 3]
c = CountedIterator(data)
while True:
    try:
        print(next(c), c.get_count())
    except StopIteration:
        break
```


