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

#print(easypass)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
length = nr_letters + nr_symbols + nr_numbers
hardpass = ''
counter1=0 # counter for letters
counter2=0 # counter for symbols
counter3=0 # counter for numbers
for i in range(length):
    a = letters[random.randint(0, len(letters)-1)]
    b = symbols[random.randint(0, len(symbols)-1)]
    c = numbers[random.randint(0, len(numbers)-1)]
    lst = [a, b, c]

    rand=lst[random.randint(0, len(lst)-1)]
    print(rand)

    if rand in letters and counter1 != nr_letters + 1:
        hardpass += rand
        counter1 += 1
    elif rand in symbols and counter2 != nr_symbols + 1:
        hardpass += rand
        counter2 += 1
    elif rand in numbers and counter3 != nr_numbers + 1:
        hardpass += rand
        counter3 += 1
    else:
        continue

print(hardpass)
# print(a)
# print(b)
# print(c)
    