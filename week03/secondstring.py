#write a program that asks a user to input a string and outputs every second character in reverse order
#Author Brid Kennedy

from importlib_metadata import Sectioned


inputString = input ('Please enter a sentence ;')

# from https://realpython.com/reverse-string-python/ will try slice(None, None, -1) function
# to reverse the sentence and to get every second character [::2]
reversedSentence = inputString[slice(None, None, -1)][::2]
print ('Every second character in reverse of your sentence is {}'.format(reversedSentence))
