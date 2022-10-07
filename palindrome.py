def isPalindrome(s):
	x=list(s)
	y=[]
	y.extend(x)
	x.reverse()
	if(x==y):
		return True
	return False
s =input("enter the name: ")
ans = isPalindrome(s)
if ans:
	print("Yes")
else:
	print("No")
