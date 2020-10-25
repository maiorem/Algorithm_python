
num=int(input())
answer=[]
for i in range(num) :
    test_case=list(map(int, input().split()))
    aver=sum(test_case[1:])/test_case[0]
    count=0
    for j in test_case[1:] :
        if aver<j:
            count+=1
    answer.append(str("%.3f" %round(count/test_case[0]*100, 3))+"%")
for a in range(len(answer)) :
    print(answer[a])
        