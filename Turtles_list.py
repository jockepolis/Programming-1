import turtle


def moveto(t, x, y):
    """Move to a (x,y) without drawing"""
    t.penup()
    t.goto(x, y)
    t.pendown()

    
def create_turtle(x, y, heading):
    """Create a turtle at (x,y) with a specified heading"""
    t = turtle.Turtle()
    moveto(t, x, y)
    t.setheading(heading)
    t.turtlesize(1.5)
    t.shape('turtle')
    return t


ts = [create_turtle(-200, 200, 270),
      create_turtle(-200, -200, 0),
      create_turtle(200, -200, 90),
      create_turtle(200, 200, 180)]

while ts[0].distance(ts[1]) > 10:
    for t in ts:
        t.forward(5)
    
    for i in range(4):
        j = (i + 1) % 4   # index for next neighbour
        ts[i].setheading(ts[i].towards(ts[j]))
