"""
Constants
"""

ZERO = 0.0

"""
Exception texts
"""
VALUE_EXCEPTION_TEXT = lambda type, value: \
    f'The {type} value must be a positive number, got {value}'
NULL_EXCEPTION_TEXT = lambda type: \
    f'The {type} description must be filled'