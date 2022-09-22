list1=[21,13,4,196,7,9,54,6,15,3,24,56,78,23]
i=0
even=[]
odd=[]
while i<len(list1):
    if list1[i]%2==0:
        d=list1[i]
        even.append(d)
    else:
        f=list1[i]
        odd.append(f)
    i=i+1
print("even numbers are",even)
print("odd numbers are",odd)
