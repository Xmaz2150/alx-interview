#!/usr/bin/python3
"""
island_perimeter module
"""


def island_perimeter(grid):
    """
    calculates the perimeter of an island in a grid
    # Assumes there is only one piece of land
    """
    if len(grid) > 100 or len(grid[0]) > 100:
        return 0
    piece_pos = {'h': [], 'w': []}
    for row in grid:
        t = []
        for p in row:
            if p == 1:
                piece_pos['h'].append(grid.index(row))
                t.append(p)
                piece_pos['w'].append(len(t))

    h = list(set(piece_pos['h']))[-1]
    w = max(piece_pos['w'])
    return 2 * (h + w)
