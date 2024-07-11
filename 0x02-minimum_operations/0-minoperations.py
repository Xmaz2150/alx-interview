#!/usr/bin/python3
"""
minop module
"""
import math


def minOperations(n: int) -> int:
    """
    returns min operations required to copy char
    as fewest numbers as possible
    #NB (Just mimicked the order of exalmple)
    """
    """
    derived from by having a[0] cp'd to make a[1]
    cp'd first char twice
    """
    p_op = 2

    if n % 2 != 0:
        """ pst'd single char again to get a[2] """
        p_op += 1
    else:
        f_d = math.floor((n/10) % 10)
        s_d = math.floor(n % 10)

        if (f_d + s_d) % 2 != 0:
            p_op += 1

    tmp = p_op
    c = p_op
    while 1:
        tmp += p_op
        c += 1
        if tmp == n:
            break

    return c + 1
