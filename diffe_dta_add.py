l=['8',9,11.9,22,'27']
i=0
s=0
while i<len(l):
    b=l[i]
    if type(b)==str:
        c=int(b)
        s=s+c
    else:
        s=s+b
    i=i+1
print(s)
k=int(s)
print(k)
