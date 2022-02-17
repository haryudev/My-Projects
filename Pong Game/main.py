from turtle import Screen
from rackets import Racket
from net import Net
from ball import Ball
from score import Score
import time
screen = Screen()

# Screen setup
game_working = True
while game_working:
    screen.bgcolor('black')
    screen.setup(width=800, height=600, startx=None, starty=None)
    screen.title('Pong')
    screen.tracer(0)
    # Game Setup

    #   Score
    point_1 = 0
    point_2 = 0
    score_player_1 = Score(60)
    score_player_2 = Score(-60)
    score_player_2.scoring(point_2)
    score_player_1.scoring(point_1)
    #   Net Setup

    net = Net()

    #   Ball Setup
    ball = Ball()

    #   Racket 1
    racket1 = Racket(position_x=350, position_y=0)
    screen.listen()
    screen.onkeypress(racket1.racket_moving_up, "Up")
    screen.onkeypress(racket1.racket_moving_down, "Down")

    #   Racket 2
    racket2 = Racket(position_x=-350, position_y=0)
    screen.onkeypress(racket2.racket_moving_up, "w")
    screen.onkeypress(racket2.racket_moving_down, "s")

#   Game
    game_is_on = True
    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move_up()

    #   Bouncing
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        if ball.distance(racket1) < 50 and ball.xcor() > 330 or ball.distance(racket2) < 50 and ball.xcor() < -330:
            ball.bounce_x()

    #   Pointing
        if ball.xcor() > 350:
            point_2 += 1
            score_player_2.scoring(point_2)
            ball.reset_position()

        if ball.xcor() < -350:
            point_1 += 1
            score_player_1.scoring(point_1)
            ball.reset_position()

    #   Ending Game
        if point_1 == 6:
            score_player_1.game_over(winner='1')
            game_is_on = False
        elif point_2 == 6:
            score_player_2.game_over(winner='2')
            game_is_on = False
    replay = screen.textinput('Replay', 'Do you want to play again?')
    if replay.lower() == "sim":
        screen.clear()
        game_is_on = True
    else:
        game_working = False
screen.exitonclick()
