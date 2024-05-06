#!/usr/bin/python3
""" Documentation """


def validUTF8(data):
    """
    Determines if a given list of
    integers represents a valid UTF-8 encoding.

    Args:
        data (list[int]): The list of
        integers representing the UTF-8 encoding.

    Returns:
        bool: True if the encoding is valid, False otherwise.
    """
    n = 0
    for v in data:
        if n > 0:
            if v >> 6 != 0b10:
                return False
            n -= 1
        elif v >> 7 == 0:
            n = 0
        elif v >> 5 == 0b110:
            n = 1
        elif v >> 4 == 0b1110:
            n = 2
        elif v >> 3 == 0b11110:
            n = 3
        else:
            return False
    return n == 0
