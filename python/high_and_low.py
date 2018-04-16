#!/usr/bin/env python3

def high_and_low(numbers):
    ints = list(map(int, numbers.split()))
    high_and_low_int = [sorted(ints)[i] for i in [-1,0]]
    res = ' '.join(map(str,high_and_low_int))
    return(res)
