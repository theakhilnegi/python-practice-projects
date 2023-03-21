import random
t=("s","p","x")
def rndm():
    a=random.randint(0,2)
    return t[a]

c_list=[]
a_list=[]

for i in range(7):
    c = rndm()
    print(f"[.]chance remaining : {7-i}")
    a = input("[.]Enter from stone : s \npaper : p\nsicsor : x\n").lower() 
    if (c=="s") and (a=="p"):
        print("        You win a point!!!🤪")
        a_list.append("1") 
    elif (c=="s") and (a=="s"):
        print("       Ohhh...  Its a Draw...😑")
    elif (c=="s") and (a=="x"):
        print("        You loose a point!!!😞")
        c_list.append("1")
    elif (c=="p") and (a=="x"):
        print("        You win a point!!!🤪")
        a_list.append("1") 
    elif (c=="p") and (a=="p"):
        print("       Ohhh...  Its a Draw...😑")
    elif (c=="p") and (a=="s"):
        print("        You loose a point!!!😞")
        c_list.append("1")
    elif (c=="x") and (a=="s"):
        print("        You win a point!!!🤪")
        a_list.append("1") 
    elif (c=="x") and (a=="x"):
        print("       Ohhh...  Its a Draw...😑")
    else:
        print("        You loose a point!!!😞")
        c_list.append("1")
    print(f"Your selection is {a} and computer is {c}")

if len(a_list)>len(c_list):
    print(f"Congratulations!!!    YOU WON...😆😎😁🥳 and your score is \n{len(a_list)}")

elif len(a_list)==len(c_list):
    print(f"Shit...   Its draw...😣😯 and your score is \n{len(a_list)}")
else:
    print(f"BAD LUCK...    YOU LOSE😨☹🥺 and your score is \n{len(a_list)}")