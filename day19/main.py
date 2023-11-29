import random
from turtle import Turtle, Screen

# tim = Turtle()
screen = Screen()

#
# def move_forward():
#     tim.forward(10)
#
#
# def move_backward():
#     tim.backward(10)
#
#
# def turn_right():
#     tim.right(10)
#
#
# def turn_left():
#     tim.left(10)
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# screen.listen()
# screen.onkey(key='w', fun=move_forward)
# screen.onkey(key='s', fun=move_backward)
# screen.onkey(key='a', fun=turn_right)
# screen.onkey(key='d', fun=turn_left)
# screen.onkey(key='c', fun=clear)
# screen.exitonclick()

screen.setup(width=500, height=400)
race_on = False
bet = screen.textinput("Who will win the race?", "Enter a colour: ")
colours = ["red", "yellow", "green", "blue", "purple", "orange"]
turtles = []
x = -240
y = -100
for i in colours:
    a = Turtle("turtle")
    a.color(i)
    a.penup()
    a.goto(x=x, y=y)
    y += 30
    turtles.append(a)
if bet:
    race_on = True

while race_on:
    for i in turtles:
        i.forward(random.randint(0, 10))
        if i.xcor() >= 230:
            race_on = False
            if bet == i.pencolor():
                print("You have won.")
            else:
                print("You have lost")
            print(f"The winning color is {i.pencolor()}")
screen.exitonclick()
