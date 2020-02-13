#write a program that outputs whether or not today is a weekday


week_day = ['Monday','Tuesday', 'Wednesday' ,'Thursday','Friday' , 'Saturday ','Sunday']
#week_end = ['Saturday','Sunday']

import datetime 

# split function splits the enter date into
#date,month,year and then the map function changes it into integers

i = list(map(int, input ("Enter Date \n\n\n").split ('/')))

# the variable day stores info (0 - 6) as integers#. and .weekday() returns the day of 
#the week as integer

day=datetime.date (i [2],i [1],i[0]).weekday()
print(week_day [day])





#print ((week_day ), format ("yes, unfortunately its a week day"))

#week_end=datetime.date (i[2],i[1],i[0]).weekday()

#print (( week_end, format (" It is the weekend :,Yay")
