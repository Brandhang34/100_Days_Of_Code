from tkinter import *

def button_clicked():
    converted = str(round(mile_to_km(int(input.get())), 2))
    value.config(text=converted)

def mile_to_km(miles):
    return(miles * 1.609344)
    

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

#Entry
input = Entry(width = 10)
input.grid(column=2, row=0)

#Label

miles = Label(text="Miles", font=("Arial", 12, "bold"))
miles.grid(column=3, row=0)

isequal = Label(text="is equal to", font=("Arial", 12, "bold"))
isequal.grid(column=1, row=1)

value = Label(text="0", font=("Arial", 12, "bold"))
value.grid(column=2, row=1)

km = Label(text="Km", font=("Arial", 12, "bold"))
km.grid(column=3, row=1)

#Button

button = Button(text="Calculate", command=button_clicked)
button.grid(column=2, row=3)

window.mainloop()

