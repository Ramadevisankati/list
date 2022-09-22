list1=['1', '2', '3', '4', '5', '6', '7', '8'] #['12', '34', '56', '78']
i=0
l=[]
while i<len(list1)-1:
    a=list1[i]+list1[i+1]
    i=i+2
    l.append(a)
print(l)
