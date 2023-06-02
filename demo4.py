from colored import bg , fg , attr

def text_colored():
    color_number = input("Chose Color Numbers from 0 To 255 : ")
    text = input("Enter Your Text : ")
    print(f"{fg(int(color_number))} {text} {attr(0)}")


text_colored()


