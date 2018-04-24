# https://www.codewars.com/kata/52597aa56021e91c93000cb0/solutions/python
move_zeros = lambda array: [x for x in array if x != 0 or x is False] + [x for x in array if x == 0 and x is not False]
