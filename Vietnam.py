import turtle

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
    t.fillcolor(color)
    t.begin_fill()
    for dist in [width, height, width, height]:
        t.forward(dist)
        t.left(90)
    t.end_fill()

def pentagram(x, y, side): # Funktionen hämtad från uppgiften
    t = make_turtle(x, y)
    t.pencolor('yellow')
    t.fillcolor('yellow')
    t.begin_fill()
    t.setheading(270 + 36/2) # Gör om pentagram-forloopen så att den endast ritar ytterkurvorna för att sedan fylla
    for i in range(5):
        t.forward(side)
        t.left(90-18)
        t.forward(side)
        t.right(180-36)
    t.end_fill()

def vietnamese_flag(x, y, height): # Nya funktionen som man anropar för att printa flaggan
    width = height*1.5 # Sätter måtten enligt uppgift (2:3)
    rectangle(x, y, width, height, 'red') # Anropar rectangle-funktionen för att få en stor röd rektangel
    pentagram(0, 85, 65) # Anropar den modifierade pentagram-funktionen

print(vietnamese_flag(-225, -150, 300)) # Anropar funktionen med rimliga mått
input()