# weekday.py
# Author: Robert O'Brien-Monk
# Outputs if today is a weekday or not
# Research https://www.w3schools.com/python/python_datetime.asp

import datetime

# get todays date
day = datetime.datetime.today()

#get the full day name
week_day= day.strftime("%A")

the_weekdays=["Monday", "Tuesday","Wednesday","Thursday","Friday"]

# check if day name is a weekday
if week_day in the_weekdays:
    print("Yes, today is a weekday!")
else:
    print("We are in the weekend!")