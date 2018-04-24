# https://www.codewars.com/kata/5544c7a5cb454edb3c000047/train/python

from math import log

def bouncingBall(h, bounce, window):
    return(-1 if (h <= 0 or bounce <= 0 or bounce >= 1 or window <= 0 or window >= h) else 1 + 2 * int(log(window / h) / log(bounce)))

