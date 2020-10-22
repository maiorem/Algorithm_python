def recursive(x) :
    if x < 1 :
        return 0
    elif x == 1 :
        return 1
    else :
        return recursive(x-1)+recursive(x-2)


def iterative(x) :
    n0 = 0
    n1 = 1
    n2 = 0
    if x == 0 or x ==1 :
        return x
    else : 
        for i in range(1, x) :
            n2 = n0 + n1
            n0 = n1
            n1 = n2
    return n2


# print(recursive(3))
print(iterative(3))