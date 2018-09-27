
import turtle
import math

tut = turtle.Turtle()

tut.speed(10)

for i in range(250):
    tut.forward(math.cos(i)*math.sqrt(i)*25)
    tut.right(math.cos(i))

turtle.done()