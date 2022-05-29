#Name: Anik Singha
#Email: anik.singha68@myhunter.cuny.edu
#Date: September 5, 2021
#Modify the program from Lab 3 to show shades of yellow

import turtle

wn = turtle.Screen()

turtle.colormode(255)       
tess = turtle.Turtle()     
tess.shape("turtle")  
tess.left(60)

for i in range(0,255,10):
     tess.forward(10)       
     tess.pensize(i)      
     tess.color(i,i,0)      

tess.left(180)
tess.penup()                
tess.forward(260)
tess.pensize(1)             
tess.color(0,0,0)           
tess.right(120)
tess.pendown()            

for i in range(0,255,10):
     tess.forward(10)        
     tess.pensize(i)        
     tess.color(i,i,0)        
