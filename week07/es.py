#Write a program that reads in a text file and outputs the number of e's it contains.
# Think about what is being asked here, document any assumptions you are making.

#The program should take the filename from an argument on the command line. 
# Ref consulted https://stackabuse.com/read-a-file-line-by-line-in-python/
#https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-7.php
# https://www.computerhope.com/issues/ch001721.htm
#mobydick text saved from https://gist.githubusercontent.com/StevenClontz/4445774/raw/1722a289b665d940495645a5eaaad4da8e3ad4c7/mobydick.txt
#arguments are also called operands or parameters in the POSIX standards. The arguments represent the 
# source or the destination of the data that the command acts on.

filename = "mobydick.txt" #filename in command line
l=input("Enter letter to be searched:") 
e = 0 #starting count for letter e
#open file in read mode, the with function takes care of closing the file
#even if an error occurs
with open(filename, "rt") as f: #read text
    for line in f: #a for loop to read each line in the file
        line = line.lower() #convert all letters to lower case
        words = line.split() #split the lines into words
        for i in words: #another for loop to work through the words list
            for letter in i: #and a for loop to work through the letters in the words
                if (letter == l): #if the user inputted letter is detected it is added to the e count
                    e = e+1
print ("The text of MobyDick has {} e's".format(e))