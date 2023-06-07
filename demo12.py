# Fuction Tack 2 Dates And Print How Many Days between 2 dates
from dateutil import parser



def diff_b2_dates(d1 , d2):
    date1 = parser.parse(d1)
    date2 = parser.parse(d2)
    diff = date2 - date1
    return diff



def main():
    date1 = input("Enter First Date (years-Month-days) : ")
    date2 = input("Enter Second Date (years-Month-days) : ")
    result_diff = diff_b2_dates(date1 , date2)
    print(f"The Diffrence Between 2 Dates Is {result_diff.days} Days.")



# Call Function
main()
    


