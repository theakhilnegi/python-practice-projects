import pyautogui 
from PIL import Image, ImageGrab
import time

def keystroke(key):
    pyautogui.keyDown(key)
    return

def action(data):
# ****************FOR TREES********************   
# ******ADJUST RANGE ACCORDING TO YOUR WEBPAGE*******
    for i in range(515,545):
        for j in range(600,675):
            if data[i,j] < 100:
                keystroke("up")
                return

# ****************FOR BIRDS********************    
    for i in range(515,545):
        for j in range(530,590):
            if data[i,j] < 100:
                keystroke("down")
                return
    return

if __name__ == "__main__":
    print("Hii Akhil Negi...   The hack has been activated in 3 seconds...")
    time.sleep(3)
    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        action(data)