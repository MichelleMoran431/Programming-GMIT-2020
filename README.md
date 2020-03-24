Weekly task 1  Introductions

I introduced myself on the Discussion forum 
I have installed the required software - 
- anaconda
-python 3.7 version 3.7 ( latest version)
- Note ++
- visual studio code
 - GIT HUB


Weekly task 2 BMI.py

A program that calculates Body Mass Index (BMI).
inputs =height (cm) and weight (kg) 
output = individuals weight /their height (m2). 
The user to input their height and weight



Weekly Task 3# Secondstring.py

A program that asks a user to input a string and outputs every second letter in reverse order.

Intially I reverse the string using [::-1] and then choose every second letter in the reversed string [::-2]

reference : Andrew Beatty review mail - suggested a less complicated way. Removing the need to  reverse sentence and just use ([[::-2]) 



Weekly task 4  Collatz.py

Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.

#current value = even then divide by 2
# next value = odd then multipy it by 3 and add one
# have the program end if the current value is one 

#reference https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff

Ensure the user inputs an number greater than 1 ,include a conditional loop to determine which calculation to use if the number is even or an odd number and to continue the loop until the value reaches 1


Weekly task 5 weekday.py

Write a program that outputs whether or not today is a weekday. An example of running this program on a Thursday is given below.

references : 
#https://docs.python.org/2/library/datetime.html
#https://www.codespeedy.com/find-the-day-of-week-with-a-given-date-in-python/
#ref :https://www.programiz.com/python-programming/if-elif-else

Create a list ( tuples) of the days of the week 
import the module DATETIME ( for manipulating dates and times) 
day=datetime.datetime.today().weekday() - reports results as integers
Ask the user to input todays date

create a loop using the days in tuple as integers. so Mon - Fri (0-4), Sat-sun ( 5,6).

Weekly task 6 squareroot.py and Newtons.py

A program that takes a positive floating-point number as input and outputs an approximation of its square root. You should create a function called sqrt that does this.

There is 2 programs created for this Task.

1. squareroot.py 
#ref#https://www.pythonpool.com/square-root-in-python/

 math module was imported
 sqrt = math.sqrt (number)
 using a loop to ensure a positive no. is entered

2. Newtons.py

references: 
# https://www.youtube.com/watch?v=ck0bTW39iXk
#https://www.youtube.com/watch?v=OAmAwSV5EGk


- to understand Newtons Method. 
- Get the user to input a number to calculate the square root of, using newtons method. 
 - Define the accuracy and the difference values to be considered prior to the successor calculation. 
 - Once successor calculation is completed - check result against the difference .
 - Reset calculation by having the guess = to the successor and return.

Create Imput details and running the defined program above 

Weekly task 7 Moby dick.py /es.py
 
ref https://www.sanfoundry.com/python-program-read-file-counts-number/


A program that reads in a text file and outputs the number of e's it contains. The program should take the filename from an argument on the command line.

Program : 
Create a Moby dick text file in visual code /desktop folder

with open ("C:\\Users\\User\\Desktop\\Programming-GMIT-2020\\moby dick.txt",'r') 

Create a loop to firstly split the text into words and check if the letter choosen by the user is equal the same letter in the text , it is added to the count.
updated on andrews advice : no need to split into words. removed 

Weekly task 8 Plots

A program that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

Using Ians presentations as references

created a Plots folder containing :
Histogram of 3 functions
ipython log
line plot of all 3 functions and individual plots



