# a="Chandini", "Sharma"
# i=0
# for i in a:
#     for j in i:
#         print(j.upper(),".",end=" ")
#         break


##2nd method##
a="chandini","sharma"
i=0
b=""
while i<len(a):
    c=a[i][0].isupper
    b=b+"."+c
    i=i+1
print(b[1:])

