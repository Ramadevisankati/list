list1=[3,8,9,4,5,0,5,0,3]
list2=[]
i=0
while i<len(list1):
    list1[i]+=3
    list2.append(list1[i])
    i=i+1
print(list2)
