import turtle
import random

def jump(t, x, y): # Funktionen hämtad från uppgiften
    t.penup()
    t.goto(x, y)
    t.pendown()

def make_turtle(x, y): # Funktionen hämtad från uppgiften
    t = turtle.Turtle()
    jump(t, x, y)
    return t

def rectangle(x, y, width, height, color): # Funktionen hämtad från uppgiften
    t = make_turtle(x, y)
    t.hideturtle()
    t.speed(0)
    t.fillcolor(color)
    t.begin_fill()
    for dist in [width, height, width, height]:
        t.forward(dist)
        t.left(90)
    t.end_fill()

def move_random(t):
    heading = t.heading()
    t.setheading(heading + random.randint((-45), 45))
    t.forward(random.randint(0, 25))
    x = t.xcor()
    y = t.ycor()
    if x > 250 or x < -250 or y > 250 or y < -250:
        t.setheading(t.towards(0, 0))


t = turtle.Turtle()
t.setheading(random.randint(0, 359))
t.speed(0)


rectangle(-250, -250, 500, 500, 'lightblue')
jump(t, random.randint(-250, 250), random.randint(-250, 250))

r = turtle.Turtle()
r.setheading(random.randint(0, 359))
r.color('red')
jump(r, random.randint(-250, 250), random.randint(-250, 250))

k = 0
for i in range(250):
    move_random(t)
    move_random(r)
    if t.distance(r) < 50:
        t.write('Close')
        k += 1

print('Turtles were close to eachother ' + str(k) + ' times!')
turtle.done()