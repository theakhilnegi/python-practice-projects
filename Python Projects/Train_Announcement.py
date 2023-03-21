import os
import pandas as pd
from gtts import gTTS
flag=1
def textToSpeech(text, filename,language):
    myobj = gTTS(text=text, lang=language, slow=False)
    myobj.save(filename)

if __name__ == "__main__":
    exlfile = pd.read_excel("announce_exl.xlsx")
    print("Your Voice recording is being processed...")
    print(exlfile)
    for index, item in exlfile.iterrows():
        sen = "Namascar kirpiya dyan di ji ye " + str(item["from"]) + " se chal kar " + str(item["via"]) + " ke raste " + str(item["to"]) + " ko jane wali gadi sankhiya " + str(item["train_no"]) + " " + str(item["train_name"]) + " kuch hi samay me platform sankhiya " + str(item["platform"]) + " par aa rahi hai"
        textToSpeech(sen,"anounce"+str(flag)+".mp3","hi")
        flag += 1