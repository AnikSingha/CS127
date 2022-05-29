#Name: Anik Singha
#Email: anik.singha68@myhunter.cuny.edu
#Date: August 25, 2021
#Modify a program to build a house using turtle graphics


import turtle
wn = turtle.Screen()           
wn.bgcolor("khaki")


tess = turtle.Turtle()          
tess.color("darkblue")
tess.pensize(5)

alex = turtle.Turtle()
alex.color("violet")
alex.pensize(5)

tess.forward(100)
tess.left(90)
tess.forward(100)
tess.left(90)
tess.forward(100)
tess.left(90)
tess.forward(100)
tess.left(90)

alex.left(90)
alex.forward(100)

alex.right(30)
alex.forward(100)
alex.right(120)
alex.forward(100)
alex.right(120)
alex.forward(100)

wn.exitonclick()
