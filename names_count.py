l=input("enter your name: ")
i=0
l1=[]
while i<len(l):
    if l[i] not in l1:
        l1.append(l[i])
    i=i+1
j=0
while j<len(l1):
    k=0
    c=0
    while k<len(l):
        if l[k]==l1[j]:
            c=c+1
        k=k+1
    print(l1[j],c)
    j=j+1