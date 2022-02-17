from turtle import Turtle


class Net():
    def __init__(self):
        new_y = -310
        for square in range(20):
            self = Turtle()
            self.penup()
            self.hideturtle()
            self.shape('square')
            self.color('white')
            self.setposition(x=0, y=new_y)
            self.shapesize(0.5, 0.5)
            new_y += 30
            self.setposition(x=0, y=new_y)
            self.showturtle()
