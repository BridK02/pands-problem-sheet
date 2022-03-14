# my solution to weekly task 02
# Author: Brid Kennedy
# BMI calculation is weight/(height/100) squared
# reference mindninjaX/Python-Projects-for-Beginners
#https://peps.python.org/pep-0498/
#https://docs.python.org/3/library/string.html#format-string-syntax
weight = float(input ("Enter your weight(kg):"))

height = float(input("Enter your height(cm):"))

BMI = weight/(height/100)**2
# reference on how to print superscript in Python https://stackoverflow.com/questions/8651361/how-do-you-print-superscript-in-python
#F-strings provide a concise, readable way to include the value of Python expressions inside strings.
print (f"The BMI is (kg/m\N{superscript two}) = {BMI:.2f}") #Fixed-point notation. For a given precision p, 
#formats the number as a decimal number with exactly p digits following the decimal point.
# With no precision given, uses a precision of 6 digits after the decimal point for float,
# and uses a precision large enough to show all coefficient digits for Decimal. 
# If no digits follow the decimal point, the decimal point is also removed unless 
# the # option is used.