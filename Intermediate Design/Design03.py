# Working with new design

import turtle
import math
design = turtle.Turtle()

design.color('green','cyan')

design.begin_fill()
design.circle(64)
design.end_fill()

design.penup()
design.right(45)
design.forward(45)
design.pendown()

turtle.done()