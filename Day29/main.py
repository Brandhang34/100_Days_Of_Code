from tkinter import *
from tkinter import messagebox
import pyperclip
import random
FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# Password Generator Project

def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    password_entry.insert(0, f"{password}")
    pyperclip.copy(f"{password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():

    if len(password_entry.get()) != 0 and len(website_entry.get()) != 0:
        isok = messagebox.askokcancel(title=website_entry.get(
        ), message=f"These are the details entered: \nEmail: {username_entry.get()} \nPassword: {password_entry.get()} \n Is it ok to save?")

        if isok == True:
            with open("data.txt", "a") as file:
                file.write(
                    f"{website_entry.get()} | {username_entry.get()} | {password_entry.get()}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
    else:
        messagebox.showwarning(
            title="Error", message="Please fill the required fields")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 95, image=logo_img)

canvas.grid(column=2, row=1)

# Website label

website = Label(text="Website:", font=(FONT_NAME, 12, "bold"))
website.grid(column=1, row=2)

# Website Entry

website_entry = Entry(width=35)
website_entry.grid(column=2, row=2, columnspan=2)
website_entry.focus()


# Email/Username label

username = Label(text="Email/Username:", font=(FONT_NAME, 12, "bold"))
username.grid(column=1, row=3)

# Email/Username entry

username_entry = Entry(width=35)
username_entry.grid(column=2, row=3, columnspan=2)
username_entry.insert(0, "SushiIsBae@yahoo.com")

# Password label

password = Label(text="Password:", font=(FONT_NAME, 14, "bold"))
password.grid(column=1, row=4)

# Password entry

password_entry = Entry(width=21)
password_entry.grid(column=2, row=4)

# Generate Password Button

generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(column=3, row=4)

# Add Button

add = Button(text="Add", width=35, command=save_password)
add.grid(column=2, row=5, columnspan=2)


window.mainloop()
