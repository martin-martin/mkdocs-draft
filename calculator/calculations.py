"""Provide several sample math calculations.

This script allows the user to print to make mathematical
calculations.

This file can also be imported as a module and contains the following
functions:

* `add` - returns the sum of two numbers
* `subtract` - returns the difference of two numbers
* `multiply` - returns the product of two numbers
* `divide` - returns the quotient of two numbers
* `power` - returns the base to the power of the exponent
* `sqrt` - returns the square root of a number
"""


def add(a: float, b: float) -> float:
    """Return the sum of two numbers.

    Args:
        a (float): first number
        b (float): second number

    Returns:
        float: sum of the first and the second number
    """

    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of two numbers.

    Args:
        a (float): minuend
        b (float): subtrahend

    Returns:
        float: the difference between the minuend minus the subtrahend
    """

    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers.

    Args:
        a (float): first number
        b (float): second number

    Returns:
        float: the product of the two numbers
    """

    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient of two numbers.

    Args:
        a (float): dividend
        b (float): divisor

    Raises:
        ZeroDivisionError: gets raised when the divisor is `0`

    Returns:
        float: the quotient
    """

    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b


def power(base: float, exponent: float = 2) -> float:
    """Return base to the power of exponent.

    Args:
        base (float): the base number
        exponent (float, optional): the exponent used. Defaults to 2

    Returns:
        float: the result of taking the base to the exponent
    """

    return base ** exponent


def sqrt(a: float) -> float:
    """Return the square root of a.

    Args:
        a (float): the number that you want to take the square root of

    Raises:
        ValueError: raises if `a` is below `0`

    Returns:
        float: the square root of `a`
    """

    if a < 0:
        raise ValueError("math domain error")
    return a ** (1 / 2)
