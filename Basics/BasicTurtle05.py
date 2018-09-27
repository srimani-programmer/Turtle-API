# Working with penup and pendown

import turtle

square = turtle.Turtle()

square.color('blue','green')
square.begin_fill()
for i in range(4):
    square.forward(100)
    square.right(90)
square.end_fill()

# changing the cursor position

square.penup()
square.forward(220)
square.pendown()

square.color('blue','cyan')
square.begin_fill()
for i in range(4):
    square.forward(100)
    square.right(90)
square.end_fill()

square.penup()
square.back(350)
square.pendown()

square.color('red','pink')
square.begin_fill()
for i in range(4):
    square.back(100)
    square.left(90)
square.end_fill()

square.penup()
square.left(90)
square.forward(225)
square.pendown()

square.color('cyan','orange')
square.begin_fill()
for i in range(4):
    square.back(100)
    square.right(90)
square.end_fill()

square.penup()
square.right(90)
square.forward(130)
square.pendown()

square.color('orange','yellow')
square.begin_fill()
for i in range(4):
    square.forward(100)
    square.right(90)
square.end_fill()

square.penup()
square.forward(220)
square.pendown()

square.color('yellow','orange')
square.begin_fill()
for i in range(4):
    square.forward(100)
    square.right(90)
square.end_fill()

turtle.done()