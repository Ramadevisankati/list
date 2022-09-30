# a=[[3,4],[9,1,2],[12,23,49],[8,9],[1,2,3,4]]
# i=0
# b=-1
# while i<len(a):
#     j=0
#     while j<len(a):
#         print(a[j][-1])
#         j=j+1
#     i=i+1
#     break

x=[2,9,11,21]
y=[24,49,8,14]

# [2,8,9,11,24,49]
i=0
# l=x+y
while i<len(y):
    
    j=0
    while j<len(y):
        if y[i]<y[j]:
            y[i],y[j]=y[j],y[i]
        j=j+1
    i=i+1
print(y)

# a=[4,6,3,1,9,24]
# i=0
# while i<len(a):
#     if a[i]%2==0:
#         print(a[i])
#     i=i+1
