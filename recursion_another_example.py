def add(a):
    if a>=1:
        add(a-1)
    print(a*2)
add(10)