start=int(input("enter the number: "))
end=int(input("enter the number: "))
count=0
for num in range(start, end ):
    if num < 0:
        count+=1
        print(num, end = " ")
print("count is:",count)
