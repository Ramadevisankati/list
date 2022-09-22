a=[1,2,3,4,5,6] #[6,1,5,2,4,3]
i=0
d=-1
l=[]
while i<len(a)/2:
    l.append(a[d])
    l.append(a[i])
    i=i+1
    d=d-1
print(l)
