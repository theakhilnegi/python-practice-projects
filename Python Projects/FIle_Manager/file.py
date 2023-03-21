import os, shutil

def folder(i):
    if i in os.listdir():
        pass
    else:
        os.mkdir(i)

print("Your current working directory is :\n"+os.getcwd())

folder_dict = {
"Images" : (".jpeg",".jpg",".png",".gif"),
"Documents" : (".docx",".pdf",".doc",".txt"),
"Videos" : (".3gp",".mp4"),
"Audios" :(".mp3",".m4a",".aac"),
"Others" : (".xxl",".html",".css"),
}

for i in os.listdir():
    file_name,extention = os.path.splitext(i)
    for x,y in folder_dict.items():
        if extention in y:
            folder(x)
            shutil.move(i,x+"\\"+i)
            break

