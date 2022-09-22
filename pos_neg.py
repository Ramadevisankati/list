#Using for loop
list1=[10, -21, 4, -45, 66, -93, 1]
pos_count=0
neg_count = 0
for num in list1:
    if num >0:
        pos_count += 1
    else:
        neg_count += 1
print("Positive numbers in the list: ", pos_count)
print("Negative numbers in the list: ", neg_count)

#using while loop
# list1 = [-10, -21, -4, -45, -66, 93, 11]
# pos_count=0
# neg_count=0
# num = 0
# while(num < len(list1)):
# 	if list1[num] >= 0:
# 		pos_count += 1
# 	else:
# 		neg_count += 1
# 	num += 1
# print("Positive numbers in the list: ", pos_count)
# print("Negative numbers in the list: ", neg_count)
