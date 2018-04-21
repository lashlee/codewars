# Your task is to construct a building which will be a pile of n cubes. The cube at the bottom will have a volume of n^3, the cube above will have volume of (n-1)^3 and so on until the top which will have a volume of 1^3.

# You are given the total volume m of the building. Being given m can you find the number n of cubes you will have to build?

# The parameter of the function findNb (find_nb, find-nb, findNb) will be an integer m and you have to return the integer n such as n^3 + (n-1)^3 + ... + 1^3 = m if such a n exists or -1 if there is no such n.

# m = sum of first n cubes
# Identity: sum of first n cubes = [n(n+1)/2]^2.
# So n(n+1) = 2sqrt(m) --> sqrt(m) is an integer.
# I took the positive sign since LHS > 0.
# n(n+1) = x --> 2n = -1 + sqrt(1 + 4x)
# Take the positive sign since LHS > 0.

# From Reddit user robinhouston, https://www.reddit.com/r/algorithms/comments/1zt63v/fast_algorithm_to_calculate_integer_square_root/cfwrb32/
def isqrt(n):
    assert n > 0
    x, y = 0, n
    while True:
        x, y = y, (y + n//y) // 2
        if x <= y: return x

def find_nb(m):
    n = (-1 + isqrt(1 + 8 * isqrt(m))) // 2
    return(int(n) if m == (n*(n+1)//2)**2 else -1)

