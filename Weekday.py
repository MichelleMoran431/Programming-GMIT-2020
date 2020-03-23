
#write a program that outputs whether or not today is a weekday
#ref# datetime module from topic 5 : lists in python presentation
#https://docs.python.org/2/library/datetime.html
#https://www.codespeedy.com/find-the-day-of-week-with-a-given-date-in-python/

week_day = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday ","Sunday")
#week_end = ['Saturday','Sunday']

import datetime 

# split function splits the enter date into
#date,month,year and then the map function changes it into integers

#i = list(map(int, input ("Enter Date \n\n\n").split ('/')))
today= (input ("todays date :"))
#takes two arguments: A function and a list. In this case the function is int, and the list is the one from above. It executes the function once on each thing in the list, and returns the result. In this casse the function is int, which converts its argument to an integer (a whole number).

# the variable day stores info (0 - 6) as integers#. and .weekday() returns the day of 
#the date of the week as integer

#day=datetime.date (i [2],i [1],i[0]).weekday() 
day=datetime.datetime.today().weekday() 


#create a loop using the days in tuple as integers
#ref :https://www.programiz.com/python-programming/if-elif-else

print(week_day[day])
#print(week_day[:6])
if day <=4: # days Mon - Fri
    print ("it's a weekday")
else:
    print("its the weekend")











#weekday = (week_day[day]) 
#weekend = week_day[5:6]
#day = week_day,(0,4)
#if day == (week_day,(0,4)):
    #print (week_day [day]), "Yes unfortunately today is a weekday"
#if day != (week_day,(0,4)):
   #print (week_day [day]), "its the weekend YAY"
