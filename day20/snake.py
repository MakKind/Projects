from turtle import Turtle


class snake:
    def __init__(self):
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]

    def create_snake(self):
        for i in range(3):
            self.add(i)

    def move(self):
        for i in range(len(self.snake_list) - 1, 0, -1):
            x = self.snake_list[i - 1].xcor()
            y = self.snake_list[i - 1].ycor()
            self.snake_list[i].goto(x, y)
        self.head.forward(10)

    def add(self, i):
        a = Turtle("square")
        a.setx(0 - i * 20)
        a.color("white")
        a.penup()
        self.snake_list.append(a)

    def extend(self, score):
        self.add(score+3)

    def reset(self):
        for i in self.snake_list:
            i.goto(1000, 1000)
        self.snake_list.clear()
        self.create_snake()
        self.head = self.snake_list[0]

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
