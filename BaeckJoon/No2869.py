N=input().split()
day=(int(N[2])-int(N[1]))/(int(N[0])-int(N[1]))
if day==int(day) :
    print(int(day))
else :
    print(int(day)+1)