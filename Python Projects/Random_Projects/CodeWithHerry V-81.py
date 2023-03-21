import os
print("Your Current Directory is",os.getcwd())
add= input("Enter your working path: ")
os.chdir(add)
print("Now your changed directory is",os.getcwd())
reserved = ("mahadev.jpg","mahadev1.jpg","mahadev3.jpg","mahadev4.jpg","akhil.jpg","akhil.3.jpg","Man's search for meaning-min.pdf","Rich Dad, Poor Dad -min.pdf")

flag=1
for i in os.listdir():
    if i in reserved:
        pass
    else:
        if i.endswith(".jpg"):
            os.rename(i,str(flag)+".jpg")
            flag += 1
        else:
            os.rename(i,i.replace(i[0],i[0].upper()))
            