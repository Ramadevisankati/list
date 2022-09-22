list1=[1, 2, 3, 4, 5, 6] #[[1,2],[2,3],[3,4],[4,5],[5,6]]
i=0
l=[]
while i<len(list1)-1:
    c=[list1[i],list1[i+1]]
    l.append(c)
    i=i+1
print(l)                
