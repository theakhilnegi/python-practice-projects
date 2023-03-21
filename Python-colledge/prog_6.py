# power of a number
def power(x,y):
    if (y==1 or y==0):
        return x
    else:
        return x*power(x,y-1)

print(power(4,3))