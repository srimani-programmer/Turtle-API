# Working with new design

import turtle

new_design = turtle.Turtle()

new_design.color('orange','dark blue')

new_design.speed(10)
new_design.begin_fill()
for i in range(36):
    new_design.forward(250)
    new_design.left(170)

new_design.end_fill()

new_design.penup()
new_design.right(90)
new_design.forward(150)
new_design.pendown()

turtle.done()