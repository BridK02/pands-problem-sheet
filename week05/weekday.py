# Write a program that outputs whether or not today is a weekday.

# Author:Brid Kennedy

# The weekday() method returns the day of the week as an integer where Monday 
# is indexed as 0 and Sunday is 6.

import datetime

week_days = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")

now = datetime.datetime.now()
day = week_days[now.weekday()] # Note the change to now.weekday()

if day == 'Tuesday' :
    print ('Yes it is tuesday, unfortunately a weekday')
else :
     print ('It is the weekend. Hurray!!')