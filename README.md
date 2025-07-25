# 📐 Geometry Toolkit – Pure Python Implementation

> A geometry utility library written from scratch in pure Python without any external libraries. Built with the intent to handle **every edge case** for line and triangle computations.  
> Developed entirely by a **pre-college student** (IIT Madras B.S. in Data Science & IIEST CSE) in just 4 days.

---

## 🔧 Features

- 📏 **Coordinate geometry methods**
- 📌 Line properties, slope, perpendiculars, midpoints
- 🔺 Triangle centers: centroid, incenter, circumcenter, orthocenter
- 🧮 Equation of line from multiple formats
- 📉 Distance from point to line
- ♾️ Internal/External point division
- 📐 Line intersection detection (parallel, perpendicular, intersecting)
- 🧪 100% tested with edge case handling
- ❌ No external libraries used — **pure Python**

---

## 📁 File Structure

```
geometry_toolkit/
├── geometry_toolkit.py      # Full Coordinate class implementation
├── test_geometry_toolkit.py # Complete test file with edge cases
├── README.md                # (You're here)
```

---

## 🧪 Run Tests

Make sure Python ≥ 3.7 is installed.

```bash
python test_geometry_toolkit.py
```

---

## 🛠 Sample Usage

```python
from geometry_toolkit import Coordinate

p1 = Coordinate(2, 3)
p2 = Coordinate(4, 5)

print(p1.slope_of_line_joining_two_point(p2))  # Output: 1.0
print(p1.midpoint_with_another_point(p2))      # Output: Coordinate(3.0, 4.0)
```

---

## 🧠 Inspiration

> This entire project was handwritten without using any online code, tutorials, or libraries — just core math and logic.

---

## 🙌 Author

**Shivam Gupta**  
📘 IIT Madras BS in Data Science  
🐍 Python & Math Enthusiast  
Created by [Shivam Gupta] (mailto:shivamguptaoff25@gmail.com)
---

## 📌 License

This project is open-source and free to use under the **MIT License**.