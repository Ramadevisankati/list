x=int(input("enter the number: "))
y=int(input("enter the number: "))
a=list(range(x,y))
i=0
s=[]
while a[i]<a[-1]:
    count=0
    j=1
    while j<=a[i]:
        if a[i]%j==0:
            count+=1
        j=j+1
    if count==2:
        s.append(a[i])
    a[i]+=1
    i=i+1
print(s)