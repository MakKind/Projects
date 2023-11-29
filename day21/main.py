from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
r_paddle = Paddle(350)
l_paddle = Paddle(-350)
top_wall = Paddle
ball = Ball()
scoreboard = Scoreboard()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.listen()
screen.onkey(key="Up", fun=r_paddle.move_up)
screen.onkey(key="Down", fun=r_paddle.move_down)
screen.onkey(key="w", fun=l_paddle.move_up)
screen.onkey(key="s", fun=l_paddle.move_down)

game_is_on = True

while game_is_on:
    screen.update()
    ball.ball_move()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 310 or ball.distance(l_paddle) < 50 and ball.xcor() < -310:
        ball.bounce_x()

    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_scoreboard()

    elif ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_scoreboard()

screen.exitonclick()
