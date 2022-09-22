n=int(input("enter the number: "))
letters=[1,2,4,6,7,8,8,5,3,3,2,1,6,8,9]
i = n
while i < len(letters):
    letters.insert(i, 'rama')
    i = i+(n+1)
print(letters)
