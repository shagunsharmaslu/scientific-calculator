
import math

def validate_numeric_input(value, allow_negative=True):
    """
    Helper function to validate if the input is numeric (int or float).
    Raises TypeError if input is not numeric. Optionally raises ValueError if negative values are not allowed.
    """
    if not isinstance(value, (int, float)):
        raise TypeError("Input must be a numeric value")
    if not allow_negative and value < 0:
        raise ValueError("Cannot compute the operation for negative numbers")

def sin(angle_in_degrees):
    validate_numeric_input(angle_in_degrees)
    return math.sin(math.radians(angle_in_degrees))

def cos(angle_in_degrees):
    validate_numeric_input(angle_in_degrees) 
    return math.cos(math.radians(angle_in_degrees))

def tan(angle_in_degrees):
    validate_numeric_input(angle_in_degrees)
    return math.tan(math.radians(angle_in_degrees))

def sqrt(value):
    validate_numeric_input(value, allow_negative=False)
    return math.sqrt(value)

def log(value):
    validate_numeric_input(value, allow_negative=False)
    return math.log(value)

def exp(value):
    validate_numeric_input(value)
    return math.exp(value)