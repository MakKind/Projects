from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed(10)
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-270, 270), random.randint(-270, 270))

    def big_refresh(self):
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("red")
        self.speed(10)
        self.refresh()
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
