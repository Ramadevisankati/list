list=[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
b=[]
i=0
while i<len(list):
    c=[list[i],list[i+1],list[i+2]]
    b.append(c)
    i=i+3
print(b)
