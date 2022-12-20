from tkinter import *

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label

my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

#Button

button = Button(text="Click me", command=button_clicked)
button.grid(column=3, row=0)

#Button2

button = Button(text="Click me", command=button_clicked)
button.grid(column=2, row=1)

#Entry
input = Entry(width = 10)
input.grid(column=4, row=3)

button = Button(text="Click me", command=button_clicked)

window.mainloop()

