 #build the function for square root using "Newton's method for square roots"
# https://www.youtube.com/watch?v=ck0bTW39iXk
#https://www.youtube.com/watch?v=OAmAwSV5EGk

# Defining the function of squareroot 

    
    #n = number to calculate squareroot of 
    #acc = the accuracy of the guess result to the calculated root value

def squareroot(n,acc):
    guess = n
    acc = 0.000001 
    diff = 1000
    while (diff > acc): # a loop that states that while difference i greater than taccurcay , do the following steps.

        successor = ((guess +(n/guess))/2.0) #identify a solution to the question which what is the squareroot
        diff = abs (successor-guess) # rest the value of difference ( abs gives a positive value)
        guess = successor # telling the function to reset the value of guess after diff calculation giving a new value to successor
    return successor

# ask the user to input a n value to calculate squareroot of  ?

n = float( input(" Enter the number to calculate the squareroot of : "))


# running the program using function specified above
#enter accuracy in commas
acc = ("0.000001")
newtons = squareroot ( n, acc)
print ("the newtons squareroot of" ,n , "to accuracy of",acc, "is" ,newtons)