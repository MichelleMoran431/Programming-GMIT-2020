Week 1 

I introduced myself on the Discussion forum 
I have installed the required software - 
- anaconda
-python 3.7 version 3.7 ( latest version)
- Note ++
- visual studio code
 - GIT HUB

Week 2 #

Weekly task 2

To Write a program that calculates Body Mass Index (BMI).
inputs =height (cm) and weight (kg) 
output = individuals weight /their height (m2). 

asking the user to input their height and weight
ensure the correct units are calculated : m*m for height
Calculation  = weight/(height*height) ( include a round to ensure precision)
print = output the BMI


Week 3# 

Weekly task 3 Secondstring.py

A program that asks a user to input a string and outputs every second letter in reverse order.

Intially I reverse the string using [::-1] and then choose every second letter in the reversed string [::-2]

reference : Andrew Beatty review mail - suggested a less complicated way. Removing the need to  reverse sentence and just use : 
print ("This is my sentence with every second letter in reverse order :",sentence[::-2])


Weekly task 4

Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.

$ python collatz.py
Please enter a positive integer: 10
10 5 16 8 4 2 1


#current value = even then divide by 2
# next value = odd then multipy it by 3 and add one
# have the program end if the current value is one 

#reference https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff

Ensure the user inputs an number greater than 1 ,include a conditional loop to determine which calculation to use if the number is even or an odd number and to continue the loop until the value reaches 1


Weekly task 5

Write a program that outputs whether or not today is a weekday. An example of running this program on a Thursday is given below.

$ python weekday.py
Yes, unfortunately today is a weekday.
An example of running it on a Saturday is as follows.

$ python weekday.py
It is the weekend, yay!

references : 
#https://docs.python.org/2/library/datetime.html
#https://www.codespeedy.com/find-the-day-of-week-with-a-given-date-in-python/

Create a list ( tuples) of the days of the week 
import the module DATETIME ( for manipulating dates and times)

i = list(map(int, input ("Enter Date \n\n\n").split ('/'))) - using map to use two functions int and input. to split and change the date into integers
create a loop using the days in tuple as integers
#ref :https://www.programiz.com/python-programming/if-elif-else

Weekly task 6

Write a program that takes a positive floating-point number as input and outputs an approximation of its square root. You should create a function called sqrt that does this.

$ python squareroot.py
Please enter a positive number: 14.5
The square root of 14.5 is approx. 3.8.

program : 
import math

number = float (input ("Enter a number to find the square root:"))
sqrt = math.sqrt (number)
#print ('the square root of {} is {} ',(number,sqrt))

if number<0: # to insure a positive floating number is entered
    print ("Please enter valid number")
else:
    print ('the square root of {} is {} ',(number,sqrt))

Program : 
Building the function : for square root using "Newton's method for square roots
Firstly to understand Newtons Method. 
Get the user to input a number to calculate the square root of, using newtons method. 
Define the accuracy and the difference values to be considered prior to the successor calculation. 
Once successor calculation is completed - check result against the difference .
Reset calculation by having the guess = to the successor and return.

Create Imput details and running the defined program above 

Weekly task 7

Write a program that reads in a text file and outputs the number of e's it contains. The program should take the filename from an argument on the command line.

$ python es.py moby-dick.txt
116960

Program : 
Create a Moby dick text file in visual code /desktop folder

ref https://www.sanfoundry.com/python-program-read-file-counts-number/
with open ("C:\\Users\\User\\Desktop\\Programming-GMIT-2020\\moby dick.txt",'r') as f : ( mode : 'r' = read)
    l=input("Enter letter to be searched:")
    k = 0
Create a loop to firstly split the text into words and check if the letter choosen by the user is equal the same letter in the text , it is added to the count.


