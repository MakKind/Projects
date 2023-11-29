from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.goto(0, 0)
        self.color("red")
        self.x_move = 0.15
        self.y_move = 0.25

    def ball_move(self):
        if -400 < self.xcor() < 400 and -300 < self.ycor() < 300:
            self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
