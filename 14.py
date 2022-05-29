#Name: Anik Singha
#Email: anik.singha68@myhunter.cuny.edu
#Date: September 5, 2021
#Ask a user for a hexadecimal number and then make a square using it

import turtle

anik = turtle.Turtle()
anik.shape("turtle")

hex = input("Please enter a 6-digit Hexadecimal number: ")

anik.color("#" + hex)

for i in range(4):
    anik.forward(100)
    anik.stamp()
    anik.left(90)

anik.forward(100)
    

