# https://www.codewars.com/kata/playing-with-digits/python
def dig_pow(n, p):
    digits = map(int, str(n))
    k = sum([y**(x+p) for x,y in enumerate(digits)])
    return(k // n if (k // n) * n == k else -1)

