word=input().upper()
alpabet=list(set(word))
al_count=[]
for letter in alpabet :
    al_count.append(word.count(letter))
if al_count.count(max(al_count)) > 1 :
    print('?')
else :
    print(alpabet[al_count.index(max(al_count))])