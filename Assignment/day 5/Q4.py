# Q4.py
# import datetime module to work with dates
import datetime as dt

# disply the current date and time
current_date_time = dt.datetime.now()
print ("Current Date and Time =", current_date_time)

# print current year
year = current_date_time.year
print("current year =", year)

# print current month
month = current_date_time.month
print("current month =", month)

# print current day
day = current_date_time.day     
print("current day =", day)

# day of week
day = current_date_time.strftime("%A")
print("day of week =", day)