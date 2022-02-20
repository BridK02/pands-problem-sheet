# Write a program that outputs whether or not today is a weekday.

# Author:Brid Kennedy
# Reference used https://stackoverflow.com/questions/63687176/how-to-check-weekday-using-if-command-in-python-using-datetime
# The weekday() method returns the day of the week as an integer where Monday 
# is indexed as 0 and Sunday is 6.

import datetime
# mapping the numbers to the days
week_days = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")

now = datetime.datetime.now()
day = week_days[now.weekday()] # The days of the week in now.weekday() will be numbered 0-6 

if day == 'Tuesday' : #Tuesday is a string ''
    print ('Yes it is tuesday, unfortunately a weekday')
else :
     print ('It is the weekend. Hurray!!')