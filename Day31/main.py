from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"


current_card = {}
dict = {}


# Create dataframe and turn into a dictionary
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    dict = original_data.to_dict(orient="records")
else:
    dict = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(dict)
    print(current_card)

    canvas.itemconfig(card_image, image=front_img)
    canvas.itemconfig(card_title, text="French", fill='black')
    canvas.itemconfig(card_word, text=current_card["French"], fill='black')
    flip_timer = window.after(3000, func=flip_card)


def right():
    dict.remove(current_card)
    data = pd.DataFrame(dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


def wrong():
    next_card()


def flip_card():
    canvas.itemconfig(card_image, image=back_img)
    canvas.itemconfig(card_title, text="English", fill='white')
    canvas.itemconfig(card_word, text=current_card["English"], fill='white')


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR)

front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(
    400, 263, image=front_img)
canvas.grid(row=0, column=0, columnspan=2)

# French column
card_title = canvas.create_text(
    400, 150, text="Language", font=("Arial", 30, "italic"), fill='black')

# Obtain a random word from the csv
card_word = canvas.create_text(
    400, 263, text="Word", font=("Arial", 50, "bold"), fill='black')

wrong_button_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_image, command=next_card)
wrong_button.grid(row=2, column=0)

right_button_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_image, command=right)
right_button.grid(row=2, column=1)

next_card()


window.mainloop()
