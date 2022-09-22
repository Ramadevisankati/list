ms=[[8,3,4],[1,5,9],[6,7,2]]
i=0
s=0
s1=0
s2=0
while i<len(ms):
    s=s+ms[i][0]
    s1=s1+ms[i][1]
    s2=s2+ms[i][2]
    i=i+1
print(s)
print(s1)
print(s2)
if s==s1==s2:
    print("True")
else:
    print("false")