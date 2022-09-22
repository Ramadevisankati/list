l1=[[1,2,3,4,5,6],[7],[8,9,10]]
i=0
sum=0
while i<len(l1):
    j=0
    while j<len(l1[i]):
        sum=sum+l1[i][j]
        j+=1
    i=i+1
print(sum)