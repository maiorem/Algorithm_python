T=int(input())
for i in range(T):
    H, W, N=map(int, input().split())
    floor=0
    ho=0
    if N%H==0:
        floor=H*100
        ho=N//H
    else:
        floor=(N%H)*100
        ho=1+N//H
    print(floor+ho)