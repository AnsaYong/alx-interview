#!/usr/bin/python3
"""
This module provides the validUTF8 function
"""


def validUTF8(data):
    """
    Determines if a given dataset represents a valid UTF-8 encoding

    Attributes:
        bytes_to_follow (int): The number of bytes that should
        follow the current byte
    Args:
        data (list): The dataset to evaluate

    Returns:
        bool: True if the dataset represents a valid UTF-8 encoding,
        False otherwise
    """
    bytes_to_follow = 0

    for byte in data:
        # Check if the byte starts a new UTF-8 character
        if bytes_to_follow == 0:
            # Count the number of bytes that should follow the current byte
            if byte >> 5 == 0b110:
                bytes_to_follow = 1
            elif byte >> 4 == 0b1110:
                bytes_to_follow = 2
            elif byte >> 3 == 0b11110:
                bytes_to_follow = 3
            elif byte >> 7:
                return False
        else:
            # Check if the current byte is a continuation byte
            if byte >> 6 == 0b10:
                bytes_to_follow -= 1
            else:
                return False

    return bytes_to_follow == 0
