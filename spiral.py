import turtle

t = turtle.Turtle()
t.color('black')
for i in range(100):
    t.forward(i)
    t.left(30 - i/10)
input()