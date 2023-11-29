import turtle
import pandas

screen = turtle.Screen()
screen.title("Guess the states Game")
image = "blank_map_of_india.gif"
screen.addshape(image)
turtle.shape(image)
states = pandas.read_csv("all_states.csv")
state_list = states.state.to_list()
guessed_list = []
while len(guessed_list) < 31:
    answer = screen.textinput(title=f"{len(guessed_list)}/31 Guessed Correctly.",
                              prompt="What's another state's name?").title()
    if answer == "Exit":
        elements_not_in_guessed_list = [element for element in state_list if element not in guessed_list]
        pandas.DataFrame(elements_not_in_guessed_list).to_csv("Missed.csv")
        break
    if answer in state_list:
        guessed_list.append(answer)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_row = states[states.state == answer]
        t.goto(int(state_row.x), int(state_row.y))
        t.write(answer)
        # t.write(state_row.state.item())


