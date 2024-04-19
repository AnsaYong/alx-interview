#!/usr/bin/python3
"""
This module contains the canUnlockAll function
which determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list): A list of lists. Each list contains
        integers representing a box and the number of the
        boxes that can be opened with the key inside the box.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    keys = [0]
    for key in keys:
        for box in boxes[key]:
            if box not in keys and box < len(boxes):
                keys.append(box)

    return len(keys) == len(boxes)
