#Name: Anik Singha
#Email: anik.singha68@myhunter.cuny.edu
#Date: September 9, 2021
#Implement psuedocode

import turtle				

turtle.colormode(255) #Allows colors to be given as 0...255

anik = turtle.Turtle()

anik.speed(0)
anik.pensize(5)

wn = turtle.Screen()
wn.bgcolor("khaki")

for i in range(36):
    anik.pencolor(0,i*7,0)
    anik.forward(10)
    anik.left(10)
    for y in range(4):
        anik.left(90)
        anik.forward(300)
        anik.backward(50)
    
