a=[5,10,20,30,40,50,3,3,215,132,215]
i=0
c=[]
# while i<len(a):
#     if a[i]>200 and a[i]<999:
#         print(a[i])
#         break
#     i=i+1
for i in a:
    # if i not in c:
    #     c.append(i)
    if i>200 and i<999:
        print(i)
        break  