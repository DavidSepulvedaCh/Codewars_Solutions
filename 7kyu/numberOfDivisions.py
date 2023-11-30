""" 
    DESCRIPTION:
        Calculate how many times a number can be divided by a given number.

        Example
        For example the number 6 can be divided by 2 two times:

        1. 6 / 2 = 3
        2. 3 / 2 = 1 remainder = 1

"""


def divisions(n, divisor):
    cont = 0
    while n >= divisor:
        x = n // divisor
        cont = cont + 1
        n = x
    return cont
