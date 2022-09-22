#even and odd count
elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# even_count=0
# odd_count=0
# for num in elements:
#     if num%2==0:
#         even_count+=1
#     else:
#         odd_count+=1
# print(even_count)
# print(odd_count)


list1 = [10, 21, 4, 45, 66, 93, 11]
even_count, odd_count = 0, 0
num = 0
while(num < len(list1)):
	if list1[num] % 2 == 0:
		even_count += 1
	else:
		odd_count += 1
	num += 1
	
print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)
