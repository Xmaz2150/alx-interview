#!/usr/bin/python3
"""
lockboxes module
"""


def canUnlockAll(boxes):
    """
    Determines if allboxes can be opened
    """
    visited = set([0])
    queue = [i for i in range(len(boxes))]

    for current_box in queue:
        box = boxes[current_box]
        if len(box) == 0:
            break

        for key in box:
            if key not in visited:
                visited.add(key)
                queue.append(key)

    if list(visited) == [i for i in range(len(boxes))]:
        return True
    else:
        return False
