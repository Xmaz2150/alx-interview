#!/usr/bin/python3

"""
pascals triangle module
"""

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)

def pascal_triangle(n):
    """
    pascals triangle builder
    """
    b = []

    if n <= 0:
        return b

    for i in range(n):
        b_i = []
        for j in range(i + 1):
            p_num = fact(i)/(fact(j) * fact(i - j))
            b_i.append(int(p_num))
        b.append(b_i)
    return b
