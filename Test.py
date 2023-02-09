import turtle
from random import randint, random # Two functions from random

def rectangle(t, x, y, w, h, color='white'):
    """Draw a rectangle"""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
    t.end_fill()
    t.fillcolor('')
    t.penup()
    t.home

def moveto(t, x, y):
    """Move to a (x,y) without drawing"""
    t.penup()
    t.goto(x,y)
    t.pendown()


def move_random(t):
    """Make random move."""
    t.left(randint(-45, 45))
    t.forward(randint(0, 30))
    if abs(t.xcor()) > 250 or abs(t.ycor()) > 250:
        t.setheading(t.towards(0,0))


def random_turtle(low=-250, high=250):
    """Creates and returns a random turtle.

       Random position,
       random heading and
       random color.
       
    """
    t = turtle.Turtle()
    moveto(t, randint(low, high), randint(low, high))
    t.setheading(randint(0, 359))
    t.speed(0)                              #
    t.color(random(), random(), random())   
    return t

# Draw the universe
p = turtle.Turtle()
p.speed(0)
rectangle(p, -250, -250, 500, 500, 'white')
p.hideturtle()

# Create a set of dizzy turtles
turtles = []
for t in range(2):
    turtles.append(random_turtle())

for i in range(1, 200):
    for t in turtles:
        move_random(t)