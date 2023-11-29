import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
turtle.colormode(255)
timmy.speed(11)

# for i in range(3, 11):
#     timmy.pencolor(random.randrange(255), random.randrange(255), random.randrange(255))
#     for j in range(0, i):
#         timmy.forward(50)
#         timmy.right(360 / i)

# direction = [0, 90, 180, 270]
# timmy.speed(10)
# timmy.pensize(10)
# for i in range(100):
#     timmy.pencolor(random.randrange(255), random.randrange(255), random.randrange(255))
#     timmy.forward(20)
#     timmy.right(random.choice(direction))


# def draw_spiro(gap):
#     for i in range(int(360 / gap)):
#         timmy.pencolor(random.randrange(255), random.randrange(255), random.randrange(255))
#         timmy.circle(100)
#         timmy.setheading(timmy.heading() + gap)
# draw_spiro(5)

# import colorgram
# rgb = []
# colour = colorgram.extract('image.jpg', 30)
#
# for i in colour:
#     rgb.append((i.rgb.r, i.rgb.g, i.rgb.b))
#
# print(rgb)

colors = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51)]
timmy.penup()
timmy.hideturtle()
timmy.setheading(225)
timmy.forward(100)
timmy.setheading(0)
for i in range(10):
    for j in range(10):
        timmy.dot(15, random.choice(colors))
        timmy.forward(30)
    if i%2 == 0:
        timmy.left(90)
        timmy.forward(30)
        timmy.left(90)
        timmy.forward(30)
    else:
        timmy.right(90)
        timmy.forward(30)
        timmy.right(90)
        timmy.forward(30)



screen = Screen()
screen.exitonclick()
