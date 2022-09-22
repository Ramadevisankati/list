a=[12300,1620,150,20,74820]
i=0
r=-1
l=[]
while i<=len(a)-1:
    if a[r] == 0:
        a[r].remove()
        i=i+1
    r=r-1
print(a)
