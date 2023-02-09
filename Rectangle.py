import turtle


class Rectangle:
    def __init__(self, width, height, xpos, ypos):
        self.width = width
        self.height = height
        self.xpos = xpos
        self.ypos = ypos

    def __str__(self):
        return f'Rectangle({self.width}, {self.height}, ' + \
            f'{self.xpos}, {self.ypos})'

    def area(self):
        return self.width*self.height

    def draw(self):
        t = turtle.Turtle()
        t.penup()
        t.goto(self.xpos, self.ypos)
        t.pendown()
        for x in range(2):
            t.forward(self.width)
            t.left(90)
            t.forward(self.height)
            t.left(90)


r = Rectangle(200, 100, 0, 0)
print(r)
r.draw()
input()