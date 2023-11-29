from turtle import Turtle

FONT = ("Courier", 8, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('red')
        self.penup()
        self.hideturtle()
        self.goto(-330, 250)
        self.level = 0
        self.update()

    def update(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def gameover(self):
        self.clear()
        self.color('black')
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
