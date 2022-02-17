from turtle import Turtle


class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setposition(x=position, y=270)

    def scoring(self, point):
        self.clear()
        self.write(arg=point, font=('Times New Roman', 20, 'normal'), align='center')

    def game_over(self, winner):
        self.color('red')
        self.setposition(0, 0)
        self.write(arg=f"PLAYER {winner} WON", font=('Times New Roman', 50, 'normal'), align='center')

