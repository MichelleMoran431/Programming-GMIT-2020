# Michelle Moran
#write a program that asks user to input a string and outputs every second letter in reverse
# first to create a simple variable



# Input sentence to be reversed : create string


sentence = (input ("Enter string :"))
 
#reverse the sentence first


sentence = sentence[::-1]

#print(sentence) uncomment this line to check the reverse if required

#Now print every second letter of the reversed sentence

print ("This is my sentence with every second letter in reverse order :",sentence[::2])

 
