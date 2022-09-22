l=["chandini","suman","savit","parveen","aman"]
i=0
b=[]
while i<len(l):
    c=l[i][0]
    b.append(c)
    i=i+1
print(b)
i=0
c=0
e=[]
a=[]
while i<len(b):
    c=b.count(b[i])
    d=b[i],c
    e.append(list(d))
    for l in e:
        if l not in a:
            a.append(l)
    i=i+1
print(a)

