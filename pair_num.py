l=[10,10,20,15,7,4,7,9,1,1,3,3,1,7,7]
i=0
c=0
j=1
b=[]
while i<len(l)-1:
    if l[i] is l[j]:
        d=l[i],l[j]
        b.append(list(d))
        c=c+1
    i+=1
    j=j+1
print(b)
print(c)
3
