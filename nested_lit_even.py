l=[[1,2],[5,8],[4,7],[3,12],[12,11]]
i=0
l2=[]
while i<len(l):
    j=0
    while j<len(l[i]):
        a=l[i][j]
        if a%2==0:
            l2.append(a)
        j=j+1
    i=i+1
print(l2)
