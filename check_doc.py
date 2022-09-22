# List1 = [1998, 2002]
# List2 = [2014, 2016]
# print ((List1 + List2)*2)

# list = [1, 2, 3, None, (1, 2, 3, 4, 5), ['Geeks', 'for',
# 'Geeks']]
# print(len(list))

# Index=int(input("num"))
# n=0
# for x in range (0,Index+1):
#     n+=x
# print(n)

list = []
n = int(input("enter the total numbers inside list.: "))
i = 1
while(i <= n):
    num = int(input("enter the numbers you want to insert into list: "))
    i +=1
    list.append(num)
print(list, " <--the given list by you is here.\n ")
list.sort()
print(list)
print(max(list))
