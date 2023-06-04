# Resize Images Whit Pillow
from PIL import Image
import PIL
import os

def resize_img(img_path , new_width):
    im = Image.open(img_path)
    width,height = im.size
    ratio = height/width
    new_height = int((ratio * new_width))
    resized_img = im.resize((new_width,new_height))
    return resized_img , im



def main():
    #extentions
    ext = ["jpg" , "png" , "jpeg" , "gif"]
    # Creation new folder
    if not os.path.exists("resized_images"):
        os.mkdir("resized_images")
    for file in os.listdir("images"):
        if file.split(".")[-1] in ext:
            resized_img , img = resize_img("images/"+file , 100)
            new_path = f"resized_images/resized-{file}"
            resized_img.save(new_path)
    print("Done .")

main()



