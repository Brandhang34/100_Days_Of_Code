import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(width=800, height=550)
turtle.shape(image)

answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?").lower()

print(answer_state)

data = pandas.read_csv("50_states.csv")

states_dictionary = data.to_dict()

print(states_dictionary)