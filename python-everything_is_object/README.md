
# 0x09. Python - Everything is Object

This project is part of the Holberton School curriculum, focusing on deepening our understanding of how Python handles variables, references, values, and memory. Specifically, we explore how *everything in Python is an object* — even primitive types.

---

## 🧠 Core Concepts

- Identity vs equality: `is` vs `==`
- Mutable vs immutable types
- Object references and memory allocation
- Python object model and type introspection

---

## 🔄 Python vs JavaScript: Value vs Reference

| Concept             | Python                              | JavaScript                              |
|--------------------|-------------------------------------|-----------------------------------------|
| Immutable types     | `int`, `float`, `str`, `tuple`, `bool`, `None` | `number`, `string`, `boolean`, `null`, `undefined` |
| Mutable types       | `list`, `dict`, `set`, `class`, `function` | `Object`, `Array`, `Function`            |
| Value equality      | `==` → compares values              | `==` or `===` (depending on type coercion) |
| Identity comparison | `is` → compares memory address      | `===` (for objects/arrays compares reference) |
| Everything is object? | ✅ Yes                          | ❌ No (primitives are not objects)        |

### Example:

```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True → Same value
print(a is b)  # False → Different objects in memory
```

```javascript
let a = [1, 2, 3];
let b = [1, 2, 3];
console.log(a === b);  // false → Different reference
```

---

## 🧬 Why is *everything* an object in Python?

Python was designed to be highly consistent and flexible. In Python:

* Every value is an object.
* Every object has:

  * A **type** (`type()`)
  * A **unique ID** in memory (`id()`)
  * A **class** that defines its behavior and attributes
* Even primitive-looking types like integers and `None` are implemented as objects under the hood.

This design allows Python to:

* Treat everything uniformly (you can introspect, extend, or even subclass most things)
* Simplify internal implementation of the language
* Enable dynamic typing and duck typing

---

## 📁 Project Structure

```
python-everything_is_object/
├── 0-answer.txt       # Task 0: Name of function that prints an object type
├── README.md          # Project description and comparison with JavaScript
```

---

## 📝 References

* [Python Data Model (official docs)](https://docs.python.org/3/reference/datamodel.html)
* [Understanding `is` vs `==` in Python](https://realpython.com/python-is-identity-vs-equality/)
* [JS Reference Types Explained](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures)
