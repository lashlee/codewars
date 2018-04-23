def tickets(people):
    till = [0,0,0]
    for x in people:
        if x == 25:  
            till = [till[0]+1, till[1], till[2]] 
        if x == 50:  
            till = [till[0]-1, till[1]+1, till[2]]
        if x == 100: 
            if till[1] > 0:
                till = [till[0]-1, till[1]-1, till[2]+1]
            else:
                till = [till[0]-3, till[1], till[2]+1]
        if any(x < 0 for x in till): 
            return("NO")
    return("YES")

