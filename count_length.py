# l=['a','b','c','a','b','b','d','d','d','d','c','a']
# l=[1,1,2,3,4,4,5,1]
s="pavanijogi"
l=list(s)
l2=[]
count=0
i=0
while i<len(s):
    count=s.count(s[i])
    a=count,s[i]
    if list(a) not in l2:
        l2.append(list(a))
    i+=1
print(l2)
