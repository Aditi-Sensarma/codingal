import calendar
import datetime

year = int(input("Enter a year whose calendar you need: "))
print(calendar.calendar(year))
print(datetime.datetime.now())