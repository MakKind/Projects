import time
from turtle import Screen
from food import Food
from snake import snake
from scoreboard import scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
snake = snake()
food = Food()
scoreboard = scoreboard()
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.score_increase()
        score = scoreboard.score
        snake.extend(score)

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    for i in snake.snake_list[1:]:
        if snake.head.distance(i) < 10:
            scoreboard.reset()
            snake.reset()
screen.exitonclick()
