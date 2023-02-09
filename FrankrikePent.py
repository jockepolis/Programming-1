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
    t.speed(0)
    t.fillcolor(color)
    t.begin_fill()
    for dist in [width, height, width, height]:
        t.forward(dist)
        t.left(90)
    t.end_fill()

def tricolore(x, y, h): # Funktionen hämtad från uppgiften
    w = h/2  	#färgfältens bredd
    rectangle(x, y, w, h, 'blue')
    rectangle(x+w, y, w, h, 'white')
    rectangle(x+2*w, y, w, h, 'red')

def pentagram(x, y, side, colorpent): # Funktionen hämtad från uppgiften
    t = make_turtle(x, y)
    t.speed(0)
    t.fillcolor(colorpent) # Behöver modifieras då pentagrammen ska vara gröna
    t.setheading(270 - 36/2)
    for i in range(2): # Denna for-loop behövs för att det ska vara raden av pentagram på två ställen
        t.begin_fill()
        for i in range(5): # Denna för att det ska vara 5 st pentagram i varje rad
            t.begin_fill()
            for i in range(5): # Denna för att det är 5 sidor i varje pentagram
                t.forward(side)
                t.left(180-36)
            t.setheading(0)
            t.penup() # Här förflyttas pennan så nästa pentagram i raden kan ritas
            t.forward(101)
            t.setheading(270 - 36/2)
            t.pendown()
            t.end_fill()
        jump(t,-200, -150) # Här hoppar pennan ned till raden under flaggan för att sen köra de två 5x5 forlooparna igen
        t.end_fill() 
print(tricolore(-150, -100, 200)) # Här anropas flaggans funktion med lämpliga mått och startpunkt
print(pentagram(-200, 250, 103, 'green')) # Här anropas pentagrammens funktion med lämpliga mått och startpunkt
input() # Denna har jag för att figuren inte bara ska försvinna när den är färdigritad