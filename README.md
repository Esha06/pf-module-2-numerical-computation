# Programming Fundamentals — Module 2 Lab: Numerical Computation

Write and run small Python programs from the command line on your own laptop:
numbers and engineering formulas, floating-point precision, strings and
f-strings, collections and nested data, the `math` module, a mini physics
engine, and automated report generation.

**Handout:** [Module 2 Lab - Student Guide - Numerical Computation.pdf](Module%202%20Lab%20-%20Student%20Guide%20-%20Numerical%20Computation.pdf)
(editable source: the `.docx` next to it)

**Needs:** the Module 1 setup — Python 3.13, a `PythonCourse` folder with `.venv`,
VS Code with its terminal set to Command Prompt. Standard library only; nothing
to install.

## Topics covered

1. Numerical computation
2. Engineering formula evaluation
3. Demonstrating floating-point precision issues
4. String manipulation and formatting
5. Collection operations
6. Creating and accessing nested lists and dictionaries
7. Standard Library: the `math` module overview
8. Python String Methods reference (docs.python.org)
9. Physics Engine Fundamentals: basic kinematic equations as Python expressions
10. Automated Report Generation: formatting raw scientific data with f-strings

## Files

**Instructor Guide:** [Module 2 Lab - Instructor Guide - Numerical Computation.pdf](Module%202%20Lab%20-%20Instructor%20Guide%20-%20Numerical%20Computation.pdf)
— timing, common errors and the exercise answer key.

The `module2` folder holds the finished lab files, for checking your own work
after you have typed them yourself from the handout.

| File | Handout part |
|------|--------------|
| `01_numbers.py` … `08_string_methods.py` | Parts 2–9 |
| `physics.py`, `09_kinematics.py` | Part 10 — kinematics and time-step simulation |
| `report.py`, `10_report.py` | Part 11 — report generation (writes `report.txt`) |
| `test_module2.py` | Part 12 — unit tests |

## Run

```bat
cd PythonCourse
.venv\Scripts\activate
cd module2
python 09_kinematics.py
python -m unittest -v test_module2
```

The tests should end with `Ran 9 tests ... OK`.

## Version

Draft v0.1 for instructor review. Every program and expected output in the
handout was run on Windows 10 with Python 3.13.15 in a `.venv` from Command
Prompt on 26 Sep 2026.
