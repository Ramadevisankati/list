l="My Name Is Ramadevi"
l2=list(l)
i=-1
r=''
while i>=-len(l2):
    j=-1
    while j>=-len(l2[i]):
        r=r + l2[i][j]
        j=j-1
    r=r+""
    i=i-1
print(r)
