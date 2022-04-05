#Write a program that reads in a text file and outputs the number of e's it contains.
# Think about what is being asked here, document any assumptions you are making.

#The program should take the filename from an argument on the command line. 
# Ref consulted https://stackabuse.com/read-a-file-line-by-line-in-python/
#https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-7.php
# https://www.computerhope.com/issues/ch001721.htm
#mobydick text saved from https://gist.githubusercontent.com/StevenClontz/4445774/raw/1722a289b665d940495645a5eaaad4da8e3ad4c7/mobydick.txt
#arguments are also called operands or parameters in the POSIX standards. The arguments represent the 
# source or the destination of the data that the command acts on.


#open file in read mode
from cmath import e
from itertools import count
from sympy import E

def letterFrequency(fileName, letter):
#open file in read mode
    file = open(fileName, "r")

#read the content of file
    data = file.read()

#declare count variable
    count=0

#iterate through each character
    for char in data:

    #compare each character with "e"
        if char == letter:
            count += 1



#return letter count
    return count

#call function and display the letter count
print(letterFrequency("mobydick.txt","e"))
print(letterFrequency("mobydick.txt","E"))