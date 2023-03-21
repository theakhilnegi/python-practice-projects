# G.C.D. of two numbers
def gcd(x, y):
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small+1):
        if((x % i == 0) and (y % i == 0)):
            temp = i 
    return temp

print("G.C.D. is", gcd(32,60))