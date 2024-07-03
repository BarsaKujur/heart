import math
from turtle import *


# Set up the screen
screen = Screen()
screen.setup(width=400, height=400)

# Create a turtle for writing
pen = Turtle()
pen.penup()
pen.goto(0, 240)  # Position the turtle at the top center
pen.pendown()

pen.color("purple")
# Write the text
pen.write("Here's your heart, Thanks for the purchase :)", align="center", font=("Arial", 16, "bold"))

# Hide the turtle
pen.hideturtle()



def hearta(k):
    return 15*math.sin(k)**3
def heartb(k):
    return 12*math.cos(k)-5*\
        math.cos(2*k)-2*\
        math.cos(3*k)-\
        math.cos(4*k)
        
        
speed(10000)
bgcolor("black")
for i in range(600):
    goto(hearta(i)*20,heartb(i)*20)
    for j in range(5):
        color("#f73487")
    goto(0,0)
    
 

  
# Hide the turtles
hideturtle()
hideturtle()

# Keep the window open
done()