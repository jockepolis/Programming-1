# Scriptet för sköldpaddorna
import turtle

color = str(input('Vilken färg ska triangeln ha? '))
side = float(input("Sidlängd: "))
t = turtle.Turtle()
t.color(color)
t.fillcolor(color)
t.begin_fill()
for i in range(3):
    t.forward(side)
    t.left(120)
t.end_fill()
input()
