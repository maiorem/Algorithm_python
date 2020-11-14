X=int(input())
line=1
while X>line:
    X-=line
    line+=1
a=X
b=line-X+1
if line%2==1:
    a=b
    b=X
print(str(a)+"/"+str(b))