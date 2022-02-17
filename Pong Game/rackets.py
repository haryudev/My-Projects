from turtle import Turtle


class Racket(Turtle):
    def __init__(self, position_x, position_y):
        super().__init__()
        self.shape('square')
        self.hideturtle()
        self.penup()
        self.color('white')
        self.shapesize(5, 1)
        self.setposition(x=position_x, y=position_y)
        self.showturtle()

    def racket_moving_up(self):
        new_y = self.ycor() + 25
        if self.ycor() <= 240:
            self.goto(y=new_y, x=self.xcor())
        else:
            None

    def racket_moving_down(self):
        new_y = self.ycor() - 25
        if self.ycor() >= -240:
            self.goto(y=new_y, x=self.xcor())
        else:
            None

