# my solution to weekly task 02
# Author: Brid Kennedy
# BMI calculation is weight/(height/100) squared
# reference mindninjaX/Python-Projects-for-Beginners

weight = float(input ("enter your weight(kg):"))
print ("weight = {}kg".format(weight))

height = float(input("enter your height(cm):"))
print ("height = {}cm".format(weight))

BMI = weight/(height/100)**2

print (f"BMI is (Kg/m2= {BMI}")