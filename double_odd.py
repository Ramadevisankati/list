a=[1,2,3,4]
i=0
b=[]
while i<len(a):
    if len(a)%2==0:
        c=a[i]*2
    a.append(c)
    i=i+1
print(a)
