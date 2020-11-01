tel=input()
dial=['ABC','DEF','GHI','JKL', 'MNO','PQRS', 'TUV','WXYZ']
num=0
for i in range(len(tel)) :
    for alp in dial :
        if tel[i] in alp :
            num+=dial.index(alp)+3
print(num)

