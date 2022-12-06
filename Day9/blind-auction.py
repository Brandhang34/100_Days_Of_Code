import os
import art

print(art.logo)
print("Welcome to the secret auction program.")
dictionary_list = []
end = False

def Add_Into_Dictionary (name, price):
    add_dictionary = {"name": name, "price": price}
    dictionary_list.append(add_dictionary)

def Highest_Bidder (list):
    highest_bid=0
    name = ''
    for dictionary in list:
        if int(dictionary["price"]) > highest_bid:
            highest_bid = int(dictionary["price"])
            name = dictionary["name"]
    print(f"The winner is: {name}" + f" with a bid of ${highest_bid}")
        

while(not(end)):
    name = input("What is your name?: ")
    price = input("What's your bid?: $")

    Add_Into_Dictionary(name, price)



    cont = input("Are there any other bidders? 'y' or 'n'")
    if cont == "n":
        end=True
        Highest_Bidder(dictionary_list)
    else:
        os.system('cls||clear')