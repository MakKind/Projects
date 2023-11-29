from turtle import Turtle

Alignment = "center"
Font = ("Courier", 12, "normal")



class scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        with open("highscore.txt") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.update_scoreboard()

    def score_increase(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=Alignment, font=Font)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.update_scoreboard()
            with open("highscore.txt", mode='w') as test:
                test.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()
