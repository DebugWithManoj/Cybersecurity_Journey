# Day 6 — Small OOP: Student Class

## Overview
This project demonstrates basic Object-Oriented Programming (OOP) concepts in Python.  
It defines a `Student` class with instance variables and methods, creates multiple student objects, and prints their details.

## Class Structure

**Student Class**
- **Instance Variables:**
  - `name` : Name of the student
  - `roll` : Roll number
  - `marks` : List of subject marks
- **Methods:**
  - `total()` : Returns the total marks of the student
  - `average()` : Returns the average marks of the student
  - `__str__()` : Returns a formatted string of student details

## Usage
- Create `Student` objects with name, roll number, and marks.
- Use `print(student_object)` to display all details.

### Example:

```python
student1 = Student("Manoj", 101, [85, 90, 78])
student2 = Student("Amit", 102, [92, 88, 79])
print(student1)
print(student2)

Output:

Student Name: Manoj
Roll Number: 101
Marks: [85, 90, 78]
Total Marks: 253
Average Marks: 84.33

Student Name: Amit
Roll Number: 102
Marks: [92, 88, 79]
Total Marks: 259
Average Marks: 86.33


