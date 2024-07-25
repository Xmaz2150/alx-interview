#!/usr/bin/python3
"""
validUTF8 module
"""


def validUTF8(data):
    """
    Validates UTF-8 encoding of:
    data (list): List of integers representing bytes
    Returns:
        bool: True if data is valid UTF-8 encoded, otherwise False
    """
    remaining_bytes = 0

    for num in data:
        byte = num & 0xFF

        if remaining_bytes:
            if byte >> 6 != 0b10:
                return False
            remaining_bytes -= 1
        else:
            if byte >> 5 == 0b110:
                remaining_bytes = 1
            elif byte >> 4 == 0b1110:
                remaining_bytes = 2
            elif byte >> 3 == 0b11110:
                remaining_bytes = 3
            elif byte >> 7:
                return False

    return remaining_bytes == 0
