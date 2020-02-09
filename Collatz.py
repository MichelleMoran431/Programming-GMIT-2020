# Create a program to ask the user to input any postive integer and out the successive values 
#of the following calculation
#current value = even then divide by 2
# next value = odd then multipy it by 3 and add one
# have the program end if the current value is one 

#reference https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff



def collatz(x):
    seq = [x]
    if x < 1: 
        return []

    if x % 2 == 0: #  even number
            x = x/2
            print (int(x))
            return (x)
    elif x % 2!=0: #  odd number       
            x = 3 * x + 1 
            print (int(x))         
            return (x)
     
x = int(input('print num:'))

while True:
    x = collatz(int(x))
    if x == 1:

        break
        #takes user input


 

     
