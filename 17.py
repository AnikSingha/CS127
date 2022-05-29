#Name: Anik Singha
#Email: anik.singha68@myhunter.cuny.edu
#Date: September 6, 2021
#Implement pseudocode

import turtle

num_stamps = int(input("Enter number of stamps the turtle will print: "))
t = turtle.Turtle()
t.shape("circle")
turtle.colormode(255)
t.penup()
# t.speed(0)
steps, red, green, blue = 10, 186, 164, 145
t.color(red, green, blue)

for i in range(num_stamps):
    t.stamp()
    steps += 2

    if red + 3 <= 255 and green + 3 <= 255 and blue + 3 <= 255:
        red, green, blue = red + 3, green + 3, blue + 3
        
    t.color(red, green, blue) 
    t.forward(steps)
    t.right(24)
