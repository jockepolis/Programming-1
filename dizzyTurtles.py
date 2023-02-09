import turtle
from random import randint 

def jump(t, x, y): # Funktionen hämtad från uppgiften
    t.penup()
    t.goto(x, y)
    t.pendown()

def make_turtle(x, y):
    t = turtle.Turtle()
    jump(t, x, y)
    return t

def rectangle(t, x, y, width, height, color): # Funktionen hämtad från uppgiften
    t = make_turtle(x, y)
    t.hideturtle()
    t.speed(0)
    t.fillcolor(color)
    t.begin_fill()
    for dist in [width, height, width, height]:
        t.forward(dist)
        t.left(90)
    t.end_fill()

def move_random(t): # Funktionen gör att paddorna rör sig slumpmässigt enligt uppgift
    t.left(randint(-45, 45))
    t.forward(randint(0, 25))
    if abs(t.xcor()) > 250 or abs(t.ycor()) > 250: # Om någon padda befinner sig utanför kvadraten, gå tillbaks mot origo
        t.setheading(t.towards(0,0))

t = turtle.Turtle() # Skapa första paddan, den svarta
t.setheading(randint(0, 359))
t.speed(0)

q = turtle.Turtle() # Skapar en padda för att rita upp rektangeln
q.speed(0)
rectangle(q, -250, -250, 500, 500, 'lightblue')
q.hideturtle()
jump(t, randint(-250, 250), randint(-250, 250))

r = turtle.Turtle() # Skapar den andra paddan, den röda
r.speed(0)
r.setheading(randint(0, 359))
r.color('red')
jump(r, randint(-250, 250), randint(-250, 250))

k = 0
for i in range(500): # Kör move_random för paddorna 500 gånger
    move_random(t)
    move_random(r)
    if t.distance(r) < 50: # Om de är närmre varandra än 50 l.e, skriv close
        t.write('Close')
        k += 1

print('Turtles were close to each other ' + str(k) + ' times') # Samlar ihop alla 'Close' i en sträng och ger det som output
turtle.done()
