def d(n):
    num=0
    for i in list(str(n)):
        num+=int(i) 
    return int(n)+num
constructor= []
for j in range(1,10001):
    con_num=d(j)
    constructor.append(con_num)

for k in range(1, 10001):
    if k in constructor:
        pass
    else:
        print(k)