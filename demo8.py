# Age Calculator

from datetime import date
from calendar import monthrange


def get_age():
    birth_day = input("Enter Your Birthday (day.month.year) : ").split(".")
    #new_birthday = birth_day.split(".")
    num_days_in_month = monthrange(date.today().year , date.today().month)[1]
    age_year = date.today().year - int(birth_day[2])
    age_month = date.today().month - int(birth_day[1])
    age_day = date.today().day - int(birth_day[0])
    if int(birth_day[1]) > date.today().month:
        year_to_months = (age_year * 12) + age_month
        age_year = (year_to_months - year_to_months % 12) // 12
        age_month = year_to_months % 12

    elif int(birth_day[0]) > date.today().day:
        month_to_day = (age_month * num_days_in_month) + age_day
        age_month = (month_to_day - month_to_day % num_days_in_month) // num_days_in_month
        age_day= month_to_day % num_days_in_month

        
    return f"Your Age Is {age_year} Years , {age_month} Months , {age_day} Days"



print(get_age())


