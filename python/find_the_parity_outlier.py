def find_outlier(integers): 
    initial_even_tally = [x % 2 for x in integers[0:3]].count(0)
    if initial_even_tally in [0,3]:
        return(next(x for x in integers if x % 2 != integers[0] % 2))
    else:
        if initial_even_tally == 1:
            return(next(x for x in integers[0:3] if x % 2 == 0))
        else:
            return(next(x for x in integers[0:3] if x % 2 == 1))
