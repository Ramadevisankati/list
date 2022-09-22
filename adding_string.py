list1 = ["M", "na", "i", "Rama"] 
list2 = ["y", "me", "s", "devi"]
i=0
d=[]
while i<len(list1):
    c=list1[i]+list2[i]
    d.append(c)
    i=i+1
print(d)

#####
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# remove None from list1 and convert result into list
res = list(filter(None, list1))
print(res)