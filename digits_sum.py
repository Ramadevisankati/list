test_list = [12, 67, 98, 34]
print(test_list)
l= []
for i in test_list:
	sum = 0
	for digit in str(i):
		sum += int(digit)
	l.append(sum)
print ("after sum = ",l)

