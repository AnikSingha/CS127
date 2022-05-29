#Name: Anik Singha
#Email: anik.singha68@myhunter.cuny.edu
#Date: August 28, 2021
#Ask the user for a phrase and do different string operations on it

phrase = input("Enter a phrase: " )
phrase = phrase[::-1]
print("Reversed phrase:", phrase)
phrase = phrase.upper()
words = phrase.split()
last_letters = ''
for x in words:
    last_letters += (x[-1])
print("Last letters of reversed words:", last_letters)

    
