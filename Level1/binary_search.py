def solution(L, x) :
    answer=-1
    low=0
    high=len(L)-1
    while low<=high:
        mid=(low+high)//2
        if L[mid]==x :
            answer=mid
            break
        elif L[mid]<x :
            low=mid+1
        else :
            high=mid-1
    return answer


print(solution([2,3,5,6,9,11,15], 11))