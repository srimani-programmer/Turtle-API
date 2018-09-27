# Working with color square

import turtle

square = turtle.Turtle()
square.color('red',"cyan")
square.begin_fill()
for i in range(4):
    square.forward(100)
    square.left(90)
square.end_fill()

turtle.done()