l = [3,6,5,8,1,9,7,2,4]
i=0
while i<len(l):
    j=0
    while j<len(l):
        if l[i]<l[j]:
            l[i],l[j]=l[j],l[i]
        j=j+1
    i=i+1
print(l)
