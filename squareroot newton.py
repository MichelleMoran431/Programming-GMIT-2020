#weekly task 6
# a program taking a positive floating-point number 
#as input and outputs an approximation of its square root


#import math

def newton (n):
    def f(x) : 
        return x*x-n
    #ans = x-(x*x-n)//(2*x*x)
    def fdev (x): 
        return 2*x
    n = float (input("Enter a number to approx the square root of :"))
    sqrtroot = n 
    for i in range (1,21): (sqrtroot)
    sqrtroot = sqrtroot -f(sqrtroot)/fdev(sqrtroot)
    return sqrtroot


#N = float(input ("Enter a number to find the square root of:"))
#x = (N-(N*N-2)/(2*N))
#for i in range (20)
#sqrtroot= x*N
#print ("square root of {} is {}", (N, x))