#!/usr/bin/python3
# 102-magic_calculation.py


def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                result += a ** b / i
        except (IndexError, ValueError, TypeError):
            result = b + a
            break
    return (result)
