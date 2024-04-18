#!/usr/bin/python3

""" Documentation """


def canUnlockAll(boxes):
    """
    Determines if all the boxes in the list can be unlocked.

    Args:
        boxes (list): A list of lists representing the lockboxes.
        Each inner list contains the indices of the boxes that can be unlocked
        with the corresponding key.

    Returns:
        bool: True if all the boxes can be unlocked, False otherwise.
    """
    keys = set([0])
    visited = set()

    while keys:
        current_key = keys.pop()
        if current_key < len(boxes):
            visited.add(current_key)
            keys.update(boxes[current_key])
            keys -= visited

    return len(visited) == len(boxes)
