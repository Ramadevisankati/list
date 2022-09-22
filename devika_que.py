# a="hello"
# b=a.replace("e","o")
# print(b)

####
a=[[8,9,10],[1,2,3]]
i=0
c=0
while i<len(a):
    j=0
    while j<len(a[i]):
        c=c+a[i][j]
        j=j+1
    i=i+1
print(c)

# l="(),[],{}"
# a=input("enter the symbol: ")
# i=0
# while i<len(l):
#     if a[i]==() or a[i]==[] or a[i]=={} :
#         print("True")
#     else:
#         print("False")
#     i=i+2
    