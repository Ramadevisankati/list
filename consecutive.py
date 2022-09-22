
# l = [4, 5, 5, 5, 3, 8]
l=[1, 1, 1, 64, 23, 64, 22, 22, 22]
a = len(l)
for i in range(a - 2):
	if l[i] == l[i + 1] and l[i + 1] ==l[i + 2]:
		print(l[i],end=" ")
