#Name: Anik Singha
#Email: anik.singha68@myhunter.cuny.edu
#Date: August 31, 2021
#shifts letters by 13

import string

word = input("Enter a word: ")

new_word = ""

for x in word:
    length = len(string.ascii_uppercase)
    index = string.ascii_uppercase.find(x)
    if index + 13 < length:
        new_word += string.ascii_uppercase[index + 13]
    else:
        new_word += string.ascii_uppercase[(index + 13) - length]

print("Your word in code is", new_word)
