#Appending method
# data1=[4,"Rama",1.23,"devi"]
# data1.append("Hyderabad")
# print(data1)

#Mutable
# data1=[4,"Rama",1.23,"devi"]
# data1[3]="sankati"
# print(data1)

#deleting method
# data1=[4,"Rama",1.23,"devi","vijayawada"]
# del data1[3]              
# print(data1)

#minimum and maximum
# list1=[95,88,66,35,44,112]
# print(min(list1))
# print(max(list1))

#Count method
# list1=[95,88,66,35,44,112,35,88,35,95,35]
# print(list1.count(35))

#Insert method
# list1=[95,88,66,35,112,44,35]
# list1.insert(3,100)
# list1.insert(4,1000)
# print(list1)

#Reverse method
# list1=[22,44,33,99,66,88,77]
# list1.reverse()
# print(list1)

#Sorting method
# list1=[22,44,33,99,66,88,77]
# list1.sort()
# print(list1)

#ascending order
# list1=[22,44,33,99,66,88,77]
# list1.sort()
# list1.reverse()
# print(list1)

#indexing
# string="Ramadevi"
# print(string[0:5])

# data1=[1,"rama",1.43,"devi","sankati"]
# print(data1[1:4])


# Python3 code to demonstrate
# converting binary list to integer
# using join() + list comprehension

# initializing list
test_list = [1, 0, 0, 1, 1, 0]

# printing original list
print ("The original list is : " + str(test_list))

# using join() + list comprehension
# converting binary list to integer
res = int("".join(str(x) for x in test_list), 2)

# printing result
print ("The converted integer value is : " + str(res))

    