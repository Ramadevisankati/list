a=[[1,0,0,2,2,3,4],[0,-2,3]]
i=0
max=0
while i<len(a):
    j=0
    sum=0
    while j<len(a[i]):
        sum+=a[i][j]
        j=j+1
    i=i+1
    if sum>max:
        max=sum
print(max)
