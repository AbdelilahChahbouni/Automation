# Birthday Calculator
from time import localtime


def birthday_calculator():
    birth_date = input("Enter Your BirthDate (Months.Days ==> 12.10): ")
    new_date = birth_date.split(".")
    left_days= (int(new_date[0]) - localtime()[1]) * 30 + (int(new_date[1]) - localtime()[2]) 
    print(f"Days Left To Your Birthday Is {left_days} ")








birthday_calculator()



