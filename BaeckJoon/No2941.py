words=input()
croatia=['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for letter in croatia :
    words=words.replace(letter, '_')
print(len(words))