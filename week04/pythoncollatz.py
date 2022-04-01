# write a program that asks the user to input any positive integer and
# outputs the sucessive values of the following calculation
# at each step calculare the next value by taking the current value
#and if it is even, divide it by two, but if it is odd, multiply it by 3 and add one
# program end if the current value is one

# Author: Brid Kennedy

#refernce https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff
# user:stvensonmt on https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff
import sys
# define collatz function

def collatz(number):

    if number % 2 == 0:  #if the number is divisable by 2 return that number and loop through with the resulting number
        print(number // 2)
        return number // 2

    elif number % 2 == 1: #if the number is not divisable by 2
        result = 3 * number + 1 #multiply the number by 3 and add 1 and loop through that resulting number
        print(result)
        return result
#programs starts below with input request
n = input("Please enter a positive integer: ")
while n != 1: #if the input does not equal one
    n = collatz(int(n)) #put the number through the defined collatz function until the function returns a value of 1