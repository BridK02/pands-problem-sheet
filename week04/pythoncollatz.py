# write a program that asks the user to input any positive integer and
# outputs the sucessive values of the following calculation
# at each step calculare the next value by taking the current value
#and if it is even, divide it by two, but if it is odd, multiply it by 3 and add one
# program end if the current value is one

# Author: Brid Kennedy

#refernce https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff

import sys
# define collatz
def collatz(number):
    if number % 2 == 0:  #if the number is even
     result = number // 2  #divide the number by 2
     print (result)

    elif number % 2 == 1: #if the number is odd
        result = number * 3 + 1 #multiply by 3 and add 1
        print (result)

    while result == 1: #when the number reaches 1 exit the loop 
        sys.exit

    while result != 1: #if the result is not 1 enter the defined collatz loop
        number = result
        collatz(number)

print ('Enter a positive integer')

try:
    number = int(input())
    collatz(number)

except ValueError:
    print('Please enter a valid integer')
            

    


