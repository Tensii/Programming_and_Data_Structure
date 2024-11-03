#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers.
    Args:
        a: first number
        b: second number, defaults to 98
    Returns:
        Sum of a and b as integer
    Raises:
        TypeError: If a or b is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
