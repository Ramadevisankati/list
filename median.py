l=[1,2,3,4,17,5,7,6,7,8,9]
s=0
i=0
m=0
while i<len(l):
    s+=l[i]
    m=s//len(l)
    i=i+1
print(m)

##
# a=[1,2,3,4,5]
# i=0
# while i<len(a)/2:
#     if len(a)%2!=0:
#         b=a[i]
#     i=i+1
# print(b)