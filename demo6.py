#Function Tack Screenshot Every Minute And Save Them in New Folder in Desktop
import pyautogui
from time import sleep , localtime
import os 



def screenshot():
    counter = 1
    if not os.path.exists("/home/local-host/Desktop/folders_screens"):
        os.mkdir("/home/local-host/Desktop/folders_screens")
    while True:
        if localtime()[5] == 59:
            screen = pyautogui.screenshot()
            path =r"/home/local-host/Desktop/folders_screens/screen"+str(counter)+".png"
            screen.save(path)
            print(f"Screenshot {counter} Is Done ..")
            counter+=1
            sleep(1)
screenshot()


