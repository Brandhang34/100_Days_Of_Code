import random
import art
import game_data
import os

os.system('cls' if os.name == 'nt' else 'clear') #clears the terminal

score = 0

A = random.choice(game_data.data)
B = random.choice(game_data.data)

ongoing = True

while(True):
    print(art.logo)
    if ongoing == True and score > 0:
        print(f"You're right! Current score: {score}.") 
    elif ongoing == False:
        print(f"Sorry, that's wrong. Final score: {score}")
        break

    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")

    print(art.vs)

    print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']}")

    if input("Who has more followers? Type 'A' or 'B': ").lower() == 'a':
        if A['follower_count'] > B['follower_count']:
            score += 1
            A = B
            B = random.choice(game_data.data)
            os.system('cls' if os.name == 'nt' else 'clear') #clears the terminal
        else: 
            os.system('cls' if os.name == 'nt' else 'clear') #clears the terminal
            ongoing = False
    else:
        if A['follower_count'] < B['follower_count']:
            score += 1
            A = B
            B = random.choice(game_data.data)
            os.system('cls' if os.name == 'nt' else 'clear') #clears the terminal
        else: 
            os.system('cls' if os.name == 'nt' else 'clear') #clears the terminal
            ongoing = False