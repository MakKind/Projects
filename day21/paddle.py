from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x):
        super().__init__()
        self.x = x
        self.penup()
        self.shape('square')
        self.color('white')
        self.shapesize(5, 1)
        self.goto(x, 0)

    def move_up(self):
        if self.ycor() < 240:
            self.goto(self.x, self.ycor() + 20)

    def move_down(self):
        if self.ycor() > -240:
            self.goto(self.x, self.ycor() - 20)
