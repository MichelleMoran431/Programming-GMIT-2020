#weekly task 6
# a program taking a positive floating-point number 
#as input and outputs an approximation of its square root


import math

number = float (input ("Enter a number to find the square root:"))
sqrt = math.sqrt (number)
#print ('the square root of {} is {} ',(number,sqrt))

if number<0: # to insure a positive floating number is entered
    print ("Please enter valid number")
else:
    print ('the square root of {} is {} ',(number,sqrt))