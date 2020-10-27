def solution(n) :
    num=[]
    for i in list(str(n)) :
        num.append(int(i))
    if num[0]==0 :
        return False
    elif len(num)<=2:
        return True
    else :
        for i in range(4) :
            if (num[i+1]-num[i])==(num[i+2]-num[i+1]) :
                return True
            else :
                return False

N=int(input())
count=0
for i in range(1, N+1) :
    if solution(i)==True :
        count+=1

print(count)