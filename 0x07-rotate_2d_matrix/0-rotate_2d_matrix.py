#!/usr/bin/python3
"""
Rotate matrix module
"""


def rotate_2d_matrix(matrix):
    """
    Rotates matrix by 90 clockwise
    """
    left = 0
    right = len(matrix) - 1

    while left < right:
        for i in range(right - left):
            top = left
            bottom = right

            ''' topL to topR - stash topR '''
            tmp = matrix[top + i][right]
            matrix[top + i][right] = matrix[top][left + i]

            ''' topR to botR - stash botR '''
            tmp2 = matrix[bottom][right - i]
            matrix[bottom][right - i] = tmp

            ''' botR to botL - stash botL '''
            tmp = matrix[bottom - i][left]
            matrix[bottom - i][left] = tmp2

            ''' botL to topL '''
            matrix[top][left + i] = tmp
        right -= 1
        left += 1
