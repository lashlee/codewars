# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

from functools import reduce

def persistence_acc(n, acc):
    digits = [int(x) for x in str(n)]
    if len(digits) == 1:
        return(acc)
    else:
        return(persistence_acc(reduce(lambda x,y: x*y, digits),acc+1))

def persistence(n):
    return(persistence_acc(n,0))

