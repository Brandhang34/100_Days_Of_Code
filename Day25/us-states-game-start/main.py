import turtle
import pandas
from state import State

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(width=800, height=550)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

states_dictionary = data.to_dict()

ongoing = True
correct_state_counter = 0
states_guessed = []


while ongoing:
    answer_state = screen.textinput(
        title=f"{correct_state_counter}/50 States Correct", prompt="What's another state's name?").lower()

    for states in states_dictionary['state']:
        state = states_dictionary['state'][states]
        state_x = states_dictionary['x'][states]
        state_y = states_dictionary['y'][states]

        if answer_state == state.lower():
            # reveal on the map and add 1 to the counter
            revealed_state = State(state, state_x, state_y)
            states_guessed.append(state)
            correct_state_counter += 1
            break
        elif answer_state == 'exit':
            missing_states = [states_dictionary['state'][i] for i in states_dictionary['state']
                              if states_dictionary['state'][i] not in states_guessed]
            ongoing = False
            break


print(missing_states)
need_to_learn = pandas.DataFrame(missing_states)
need_to_learn.to_csv("list_of_states.csv")
