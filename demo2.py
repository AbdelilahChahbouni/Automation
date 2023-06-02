#Function Tackes convert Numbers To Words

from num2words import num2words

def numTowords():
    flag = True
    lang= input("Chose The Langauge :\nen : (English default)\nfr : (france)\nde : (Germany\nes : (spanish))\n ")
    while flag:
            number = input(">> ")
            if number == "q":
                flag = False
                continue
            elif number.isdigit() == False:
                continue
            print(num2words(number , lang=lang))


numTowords()



