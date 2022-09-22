# l=[1,2,3,4,5]
# i=0
# r=-1
# rev=[]
# while i<len(l):
#     rev.append(l[r])
#     rev.append(l[i])
# print(rev)

# my_list=[[1,2],[3,4],[5,6,7]]
# result=my_list[1:2:1]
# print(result)
#Output:[[5, 6, 7], [3, 4], [1, 2]]

my_list=[[1,2],[3,4],[5,6,7]]
for sub_list in my_list:
    sub_list.reverse()
print(my_list)