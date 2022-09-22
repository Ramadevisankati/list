a=[2,1,2]
b=[1,1]
i=0
while i<len(a):
    if a[i] not in b:
        print(a[i])
        break
    i=i+1
