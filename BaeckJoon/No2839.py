N=int(input())
num=0
while True :
    if N%5==0 :
        num=num+(N//5)
        break
    N=N-3
    num+=1
    if N < 0 :
        num=-1
        break

print(num)