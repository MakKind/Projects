import random
import time
from turtle import Screen
from carmanager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
cars = CarManager()
scoreboard = Scoreboard()
player = Player()
screen.setup(800, 600)
screen.tracer(0)

screen.listen()
screen.onkey(key="Up", fun=player.move_up)

game_is_on = True
cars.car_create()
i = 0
while game_is_on:
    screen.update()
    time.sleep(.1)
    cars.move()
    if player.is_at_finish_line():
        cars.update()
        scoreboard.update()
        player.reset_level()

    for car in cars.all_cars:
        if player.distance(car) < 20:
            scoreboard.gameover()
            game_is_on = False
            
    if random.randint(1, 6) % 6 == 0:
        cars.car_create()

screen.exitonclick()
