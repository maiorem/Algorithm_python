sangsu=input().split()
s_list=[]
for i in range(len(sangsu)) :
    s_list.append(sangsu[i][::-1])
print(max(s_list))