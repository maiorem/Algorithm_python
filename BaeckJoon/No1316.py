N=int(input())
groupword=[]
for i in range(N) :
    words=input()
    if list(words)==sorted(words, key=words.find) :
        groupword.append(words)
                   
print(len(groupword))