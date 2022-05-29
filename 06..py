#Name: Anik Singha
#Email: anik.singha68@myhunter.cuny.edu
#Data: August 25, 2021
#This program asks a user for a sentence and a letter and then prints the sentence three diferent times
#Once with all uppercase letter, once with all lowercase letters, and once normally.
#Lastly, it prints the number of times the letter showed up in the sentence

message = input("Enter a message: ")
letter = input("Enter a letter: ")

print(message)
print(message.upper())
print(message.lower())
print(message.count(letter))
               
