# str="coding is fun"
# l=str.split( )
# print(len(l[-1]))

str="coding is fun"
i=0
a=str.split()
while i<len(a)-2:
    print("the length of the last word",len(a[-1]))
    i+=1