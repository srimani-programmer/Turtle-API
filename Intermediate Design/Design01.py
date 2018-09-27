# Working with new design

import turtle

new_design = turtle.Turtle()
new_design.color('black','red')
new_design.begin_fill()
for i in range(8):
    new_design.forward(500)
    new_design.left(135)
new_design.end_fill()

new_design.penup()
new_design.right(90)
new_design.forward(150)
new_design.pendown()

turtle.done()