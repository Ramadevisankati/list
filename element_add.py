list1=[1,2,3,4,5,5,6,7,8,9]
i=0
l2=[]
s=-1
while i<len(list1)/2:
    a=list1[i]+list1[s]
    l2.append(a)
    i=i+1
    s=s-1
print(l2)
