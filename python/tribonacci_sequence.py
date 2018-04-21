# https://www.codewars.com/kata/556deca17c58da83c00002db/train/python

def tribonacci(signature, n):
    if n <= 3:
        return(signature[0:n])
    else:
        if signature == [0,0,0]:
            return([0] * n)
        else:
            res = signature + [0]*(n-3)
            for x in range(3,n):
                res[x] = res[x-1] + res[x-2] + res[x-3]
            return(res)

