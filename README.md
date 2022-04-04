
# Pands-Problem-sheet

A series of problems that I have been assigned to complete and push up to this GitHub repository as part of the Programming and Scripting Module in the Hons Degree in Computer Science (Data Analytics).
## Index




### Weekly Tasks 02
Write a program (called bmi.py) that calculates somebody's Body Mass Index (BMI).

The inputs are the person's height in centimetres and weight in kilograms.
The output is the calculated BMI 

Goals of this task were to practice using comments to explain our code, string format() that allows you to format selected parts of a string
and placeholders (curly brackets {}) in the text, and run the values through the format() method

### Weekly Task 03
Write a program (secondstring.py) that asks a user to input a string and outputs every second character in reverse order

Goal of this task was to practice using python interpreter built in functions and types, specifically to read in a string use a method to reverse the string and an additional method to then output everysecond letter in the reversed sentence. I did not strip the spaces from the string as this was not specified in the instructions.


### Weekly task 04
Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.

At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.

Have the program end if the current value is one.



$ python collatz.py

Please enter a positive integer: 10

10 5 16 8 4 2 1

### Weekly task 05
Write a program that outputs whether or not today is a weekday.

(You will need to search the web to find how you work out what day it is)

An example of running this program on a Thursday is given below.

$ python weekday.py
Yes, unfortunately today is a weekday.


An example of running it on a Saturday is as follows:

$ python weekday.py
It is the weekend, yay!

### Weekly task 06
Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

You should create a function called <tt>sqrt</tt> that does this.

We are asked to create our own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x).

To demonstrate that you can research and code a process.

From https://math.stackexchange.com/questions/721258/newtons-method-for-estimating-square-roots
To find a square root of a using Newton's Method, we can write:

f(x)=x<sup>2</sup>−a
This is because the roots would be:

f(x)=x<sup>2</sup>−a=0⟹x<sup>2</sup>=a⟹x=± a−−√
Apply Newton's iteration:
https://math.stackexchange.com/a/721267

$ python squareroot.py
Please enter a positive number: 14.5
The square root of 14.5 is approx. 3.8.

### Weekly task 07
Write a program that reads in a text file and outputs the number of e's it contains. Think about what is being asked here, document any assumptions you are making.

The program should take the filename from an argument on the command line. I have not shown you how to do this, you need to look it up.



$ python es.py moby-dick.txt
116960

### Weekly task 08
Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

Some marks will be given for making the plot look nice.

## Authors

- [@BridK02](https://github.com/BridK02)

## Acknowledgements

 - [readme.so](https://readme.so/editor)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)

