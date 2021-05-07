# How-To Guide

This part of the project documentation focuses on a **problem-oriented** approach. You'll tackle common tasks that you might have with the help of the code provided in this project.

## How To Add Two Numbers?

You have two numbers and you need to add them together. You're in luck! The `calculator` package can help you get this done.

Download the code from this GitHub repository and place the `calculator/` folder in the same directory as your Python script:

```text
your_project/
│
├── calculator/
│   ├── __init__.py
│   └── calculations.py
│
└── your_script.py
```

Inside of `your_script.py` you can now import the `add()` function from the `calculator.calculations` module:

```python
# your_script.py
from calculator.calculations import add
```

After you've imported the function, you can use it to add any two numbers that you need to add:

```python
# your_script.py
from calculator.calculations import add

print(add(20, 22))  # OUTPUT: 42
```

Using only one `import` statement, you're now able to add any two numbers.
