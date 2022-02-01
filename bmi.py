# my solution to weekly task 02
# Author: Brid Kennedy
# BMI calculation is weight/(height/100) squared
# reference mindninjaX/Python-Projects-for-Beginners

weight = float(input ("Enter your weight(kg):"))

height = float(input("Enter your height(cm):"))

BMI = weight/(height/100)**2
# reference on how to print superscript in Python https://stackoverflow.com/questions/8651361/how-do-you-print-superscript-in-python
print (f"The BMI is (kg/m\N{superscript two}) = {BMI}")