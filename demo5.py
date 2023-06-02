#BMI CALCULTOR 
def bmi_calcultor():
    weight = int(input("Enter Your Weight : "))
    height = float(input("Enter Your Height : "))
    while height <= 0:
        print("height musst more than zero")
        height = float(input("Enter Your Height : "))
    result = weight / (height*height)
    if result > 25.0:
        print(f"Your Body Mass Index Is {result:.2f} , This Is Considered overweight." )
    elif result > 18.5 and result < 24.9:
        print(f"Your Body Mass Index Is {result:.2f} , This Is Considered Healthy." )
    else:
        print(f"Your Body Mass Index Is {result:.2f} , This Is Considered underweight." )



bmi_calcultor()


