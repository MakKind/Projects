from turtle import Turtle

STARTING_POSITION = -280
MOVE_DISTANCE = 30
FINISH_LINE = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.reset_level()

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def reset_level(self):
        self.setheading(90)
        self.goto(0, STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > 280:
            return True
        else:
            return False
