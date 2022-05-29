#Name: Anik Singha
#Email: anik.singha68@myhunter.cuny.edu
#Date: August 25, 2021
#Write a program to generate a given image

import turtle

wn = turtle.Screen()
wn.bgcolor("khaki")

anik = turtle.Turtle()
anik.shape("turtle")
anik.fillcolor("green")
anik.pensize(3)


for x in range(6):
    anik.forward(100)
    anik.left(45)
    anik.forward(100)
    anik.left(135)
    anik.stamp()
    anik.forward(100)
    anik.left(45)
    anik.forward(100)
    anik.left(75)


    
    
       
    
