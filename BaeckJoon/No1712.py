budge=input().split()
point=0
if int(budge[2])<=int(budge[1]) :
    point=-1
else :
    point=int(budge[0])//(int(budge[2])-int(budge[1]))+1
print(point)