T=int(input())
for i in range(T) :
    test_case=list(map(str, input().split()))
    P=''
    for letter in test_case[1] :
        P+=int(test_case[0])*letter
    print(P)