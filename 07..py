#Name: Anik Singha
#Email: anik.singha68@myhunter.cuny.edu
#Data: August 25, 2021
#Ask a user to enter a message then return the corresponding unicode + 5 for each character

message = input("Enter a message: ")

for x in message:
    y = ord(x)
    print(x,"shifted by 5 characters is:", chr(y+5))
