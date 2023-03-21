# newton method for square root

def newton_methon(num,num_iters=100):
    a=float(num)
    for i in range(num_iters):
        num=0.5*(num + (a/num))
    return num

inp=int(input("Enter the number: "))
print("Square root of "+str(inp)+" is "+ str(newton_methon(inp,500)))