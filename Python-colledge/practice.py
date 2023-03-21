x=[3,64,25,75,743,84,25,2]
l=[i for i in x if i%2==0]
print(l)

s=list(filter(lambda i:i%2==0,x))
print(s)
