#Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

def unique_in_order(iterable):
    # Python3 way:
    # return([iterable[0]] + [x for x,y in zip(iterable[1:],iterable[:-1]) if x != y])
    # From https://stackoverflow.com/questions/5738901/removing-elements-that-have-consecutive-duplicates-in-python/46977206#46977206
    return([v for i, v in enumerate(iterable) if i == 0 or v != iterable[i-1]])
 
