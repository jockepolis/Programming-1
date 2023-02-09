import turtle
import math

t = turtle.Turtle()
t.speed(1)
t.hideturtle()
t.fillcolor('SkyBlue')

t.begin_fill()
for i in range(-360, 361, 10):
    x = i*math.pi/180
    t.goto(x*50, 200*math.sin(x))
t.home()
t.end_fill()
input()