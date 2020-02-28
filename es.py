
# example of counting 

#sentence ='mary had a little lamb'
#print(sentence.count('a'))


# Count the number of letter e in moby text 

# need to call moby text file

#with open ("C:\\Users\\User\\Desktop\\Programming-GMIT-2020\\moby dick.txt",'r') as f :
    #book = (f.read ())
    #result = book.count 
    #print ((f.read (),count('e'))

    #fname = input("Enter file name: ")

#l=input("Enter letter to be searched:")
#k = 0

#ref https://www.sanfoundry.com/python-program-read-file-counts-number/
 
with open ("C:\\Users\\User\\Desktop\\Programming-GMIT-2020\\moby dick.txt",'r') as f :
    l=input("Enter letter to be searched:")
    k = 0
    
    for line in f:
        words = line.split() #Each line is split into a list of words using split().
        for i in words: #loop is used to traverse through the words list and another for loop is used to traverse through the letters in the word.
            for letter in i:
                if(letter==l):#If the letter provided by the user and the letter encountered over iteration are equal, the letter count is incremented.
                    k=k+1
print("Occurrences of the letter:")
print(k)