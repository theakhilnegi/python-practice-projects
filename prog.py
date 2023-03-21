def factorial(n):
   if n == 1:
       return n
   else:
       return n*factorial(n-1)

def cou(i):
    cout=0
    i=str(i)
    for x,y in enumerate(range(len(i))):
        if i[-1-x]=="0":
            cout=cout+1
        else:
            return cout

m=int(input())
flag=2
while(1):
    fact=factorial(flag)
    flag=flag+1
    if cou(fact)==m:
        print(flag-1)
        break
