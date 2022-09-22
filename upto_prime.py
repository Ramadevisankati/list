n=int(input("enter the number: "))
i=0
a=[]
while i<=n:
    j=1
    count=0
    while j<=i:
        if i%j==0:
            count=count+1
        j=j+1
    if count==2:
        a.append(i)
    i=i+1
print(a)
