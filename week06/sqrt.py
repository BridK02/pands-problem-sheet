#Write a program that takes a positive floating-point number 
# as input and outputs an approximation of its square root.

#You should create a function called <tt>sqrt</tt> that
#  does this

#refernce used https://stackoverflow.com/questions/64613184/newtons-git 
# method-with-looping-recursion

import math #import python math module

TOLERANCE = 0.00000001
def newton(x): 
    # Returns the square root of x
    # Perform the successive approximations
    estimate = 1.0 #setting the first estimate
    while True: #initiating a while loop
        estimate = (estimate + x / estimate) / 2 #defining estimate eg 1=(1 + input number/1)
        difference = abs(x - estimate ** 2)  # defining difference as the absolute number of the input number minus the estimate number squared
        if difference <= TOLERANCE: # if the difference is less than or equal to the defined tolerance of 0.00000001
            break #then stop
    return estimate #and return estimate
def main(): #defining the main program
    # Allows the user to obtain square roots.
    while True: 
        # Receive the input number from the user
        x = input("Enter a positive number or enter/return to quit: ")
        if x == "":
             break
        x = float(x)
        # Output the result
        print("The program's estimate is", newton(x)) # outputs the result of our defined nexton calculation
        print("Python's estimate is     ", math.sqrt(x)) #comparing it to the python squareroot function result
if __name__ == "__main__": main() #dundername condition to excute the code inside the if statement
