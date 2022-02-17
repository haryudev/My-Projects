from turtle import Turtle
from random import randint

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('green')
        self.shapesize()
        self.penup()
        self.moving_list = [-10, 10]
        self.x_move = self.moving_list[randint(-1, 1)]
        self.y_move = self.moving_list[randint(-1, 1)]
        self.move_speed = 0.1

    def move_up(self):
        x_pos = self.xcor() + self.x_move
        y_pos = self.ycor() + self.y_move
        self.setposition(x_pos, y_pos)

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def bounce_y(self):
        self.y_move *= -1

    def reset_position(self):
        self.setposition(0, 0)
        self.x_move = self.moving_list[randint(-1, 1)]
        self.y_move = self.moving_list[randint(-1, 1)]
        self.move_speed = 0.1
