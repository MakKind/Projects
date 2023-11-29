# from turtle import Turtle, Screen
# # import another_module
# #
# # print(another_module.another_variable)
# timmy = Turtle()
# my_screen = Screen()
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
# print(my_screen.canvheight)
# my_screen.exitonclick()
import prettytable
from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
