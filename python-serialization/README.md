# 📄 Serialization & Deserialization in Python

## 🧠 What is Serialization?

Serialization is the process of converting a Python object into a format that can be stored (e.g., in a file or database) or transmitted (e.g., over a network). The format can later be deserialized to recreate the original object.

## 🔁 What is Deserialization?

Deserialization is the reverse process: taking serialized data and converting it back into a usable Python object.

---

## 🔹 Common Serialization Formats

### 1. **JSON (JavaScript Object Notation)**

* **Text-based**, human-readable format.
* Great for web APIs, configuration files, and cross-language communication.
* Only supports basic data types (dict, list, int, float, str, bool, None).

**Python Module**: `json`

```python
import json

# Serialize
json.dump(data, file)
# Deserialize
json.load(file)
```

**Pros**:

* Human-readable
* Language-independent

**Cons**:

* No support for custom Python objects
* Only supports basic types

---

### 2. **Pickle (Python Object Serialization)**

* **Binary format** specific to Python.
* Supports all Python objects, including custom classes.

**Python Module**: `pickle`

```python
import pickle

# Serialize
pickle.dump(obj, file)
# Deserialize
pickle.load(file)
```

**Pros**:

* Can serialize almost any Python object
* Easy to use

**Cons**:

* Not human-readable
* **Not safe** to unpickle data from untrusted sources (can execute code)
* Not cross-language compatible

---

### 3. **CSV (Comma-Separated Values)**

* Plain-text format for **tabular data** (like Excel tables).
* Each line represents a row; commas separate columns.

**Python Module**: `csv`

```python
import csv

# Reading CSV into a list of dicts
with open("file.csv", "r") as f:
    reader = csv.DictReader(f)
    data = [row for row in reader]
```

**Pros**:

* Simple and widely supported
* Human-readable

**Cons**:

* Flat structure only
* No nested data or type handling

---

### 4. **XML (eXtensible Markup Language)**

* Text-based markup format similar to HTML.
* Good for hierarchical/nested structured data.

**Python Module**: `xml.etree.ElementTree`

```python
import xml.etree.ElementTree as ET

# Writing
root = ET.Element("data")
ET.SubElement(root, "name").text = "John"
ET.ElementTree(root).write("file.xml")

# Reading
tree = ET.parse("file.xml")
root = tree.getroot()
data = {child.tag: child.text for child in root}
```

**Pros**:

* Structured and self-descriptive
* Human-readable

**Cons**:

* Verbose
* All data are stored as strings unless manually converted

---

## 🔍 Comparison Table

| Format | Readable | Custom Objects | Cross-language | Ideal Use Case           |
| ------ | -------- | -------------- | -------------- | ------------------------ |
| JSON   | ✅        | ❌              | ✅              | APIs, configs            |
| Pickle | ❌        | ✅              | ❌              | Internal Python storage  |
| CSV    | ✅        | ❌              | ✅              | Simple tables            |
| XML    | ✅        | ❌              | ✅              | Nested/hierarchical data |

---

## 🛡️ Best Practices

* ✅ Use **JSON** for cross-platform compatibility
* ✅ Use **Pickle** only for trusted internal use
* ✅ Validate input before deserialization
* ✅ Manually cast types when reading from XML or CSV

---

## 📂 Related Python Modules

* `json` — built-in JSON encoder/decoder
* `pickle` — built-in object serializer for Python
* `csv` — built-in CSV file reader/writer
* `xml.etree.ElementTree` — built-in XML processor
