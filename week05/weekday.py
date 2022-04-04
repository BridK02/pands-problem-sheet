# Write a program that outputs whether or not today is a weekday.

# Author:Brid Kennedy
# Reference used Write a program that outputs whether or not today is a weekday://stackoverflow.com/questions/63687176/how-to-check-weekday-using-if-command-in-python-using-datetime
# and https://www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.php
# The weekday() method returns the day of the week as an integer where Monday 
# is indexed as 0 and Sunday is 6.

import datetime
weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursady', 'Friday'] #Weekdays in a list
now = datetime.datetime.now().strftime('%A') #using datetime module to find current Weekday of the week:
if now in weekday: # using if and else to print required sentences
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")

