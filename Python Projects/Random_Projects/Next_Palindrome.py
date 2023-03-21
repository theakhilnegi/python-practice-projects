a=input("enter first no: ")

def palin(x):
    flag=0
    for _ in x:
        if x[flag]==x[len(x)-flag-1]:
            flag=flag+1
        else:
            return True
    return False

root=True
if palin(a):
    while root:
        a=str(int(a)+1)
        root=palin(a)
    print(a)
else:
    print(a)

