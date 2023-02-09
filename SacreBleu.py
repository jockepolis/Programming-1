import turtle

t = turtle.Turtle()
size=200
t.penup()
t.goto(-size*1.5, -size)  	# Gå till nedre vänstra hörnet
t.pendown()

colors = ['blue', 'white', 'red']
sides = [size, 2*size, size, 2*size]
for c in colors:    		# iterera över färgerna
    t.fillcolor(c)
    t.begin_fill()
    for side in sides:  	# iterera över sidorna
        t.forward(side) 	
        t.left(90)	
    t.end_fill()
    t.forward(size)		# Gå till nästa färgrand
input()