# Files Managment

import os , shutil
data_base = {"vidoes" : "mp4" , "Music" : "mp3" , "Documents" : ["doc" , "pdf"] , "archive" : ["rar" ,"gz" , "xz", "zip"] , "images" : ["png" , "jpg"]}

os.chdir("data")


# This Function To Get Available Extentions Files
def get_ext():
    ext = {item[item.rindex(".")+1:] for item in os.listdir() if "." in item}
    return ext

# Create Folders Based of Extentions 

def create_folder( data_base):
    ex = list(get_ext())
    for item in data_base:
        for ext in ex:
            if data_base[item] == ext or ext in data_base[item]:
                if os.path.exists(item) == False:
                    os.mkdir(item)

# Get Name Folder Base On Extention
def name_folder(name_ex):
    for item in data_base:
            if data_base[item] == name_ex or name_ex in data_base[item]:
                return item
                break
    return "othors"



# Move Files Into Folders
def move_files():
    create_folder(data_base)
    for name in os.listdir():
        if "." in name:
            shutil.move(name , name_folder(name[name.rindex(".") +1 : ]))




move_files()














