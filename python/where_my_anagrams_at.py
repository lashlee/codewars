# https://www.codewars.com/kata/where-my-anagrams-at/train/python

def anagrams(word, words):
    return([w for w in words if sorted(w) == sorted(word)])

