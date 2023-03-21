vowels = ['a','e','i','o','u']

file_1=open("file_2.txt")

def check(r):
    flag=0
    for i in r:
        if i in vowels:
            flag=1
            break

    if (flag==0):
        with open("file_3.txt","a") as file_2:
            file_2.write(r)


for i in file_1.readlines():
    check(i)

file_1.close()