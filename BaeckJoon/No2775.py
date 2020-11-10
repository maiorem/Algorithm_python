T=int(input())
for i in range(T) :
    k=int(input())
    n=int(input())
    v=[i for i in range(1, n+1)]
    for j in range(k) :
        for k in range(1, n) :
            v[k]+=v[k-1]
    print(v[n-1])