# import the date class from datetime
from datetime import date

# assign today to a variable
today = date.today()

# print the current date
print("Today is: ", today)

# introduce logic to deduce whether "today" is a Monday
if today.weekday() == 0:
    print("Yep, today is Monday.")
else:
    print("Nope, it's not Monday.")
