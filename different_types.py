l=[15.3,"rama","narani",61,9,12.7,"devi"]
i=0
l1=[]
l2=[]
l3=[]
while i<len(l):
    if type(l[i])==int:
        l1.append(l[i])
    elif type(l[i])==float:
        l2.append(l[i])
    elif type(l[i])==str:
        l3.append(l[i])
    i=i+1
    print(l2)
print("integers values are:",l1)
print("float values are: ",l2)
print("string values are: ",l3)
