import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "blue", "green", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def move(self):
        for car in self.all_cars:
            car.backward(self.move_speed)

    def update(self):
        self.move_speed += MOVE_INCREMENT

    def car_create(self):
        new_car = Turtle()
        new_car.penup()
        new_car.shape("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(1, 2)
        new_car.goto(380, random.randint(-250, 250))
        new_car.move_speed = STARTING_MOVE_DISTANCE
        self.all_cars.append(new_car)

