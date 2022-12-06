#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
easypass = ''

for let in range(nr_letters):
    a = random.randint(0, len(letters)-1)
    easypass += letters[a]
    
for sym in range(nr_symbols):
    b = random.randint(0, len(symbols)-1)
    easypass += symbols[b]

for num in range(nr_numbers):
    c = random.randint(0, len(numbers)-1)
    easypass += numbers[c]

print("Easy Password: " + easypass)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
hardpass = []

for let in range(nr_letters):
    hardpass.append(letters[random.randint(0, len(letters)-1)])
    
for sym in range(nr_symbols):
    hardpass.append(symbols[random.randint(0, len(symbols)-1)])

for num in range(nr_numbers):
    hardpass.append(numbers[random.randint(0, len(numbers)-1)])

random.shuffle(hardpass)

password = ''
for i in hardpass:
    password += i

print("Hard Password: " + password)
