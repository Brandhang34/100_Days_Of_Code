import random
import art

print(art.logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
if input("Choose a difficulty. Type 'easy' or 'hard': ") == "easy":
    attempts = 10
else:
    attempts = 5

#generate a random number between 1 and 100
random_num = random.randint(1,100)
print(f"Hint, the number is: {random_num}")

#for loop iterates backwards from the range of number of attempts to 1
for i in range(0, attempts):
    print(f"You have {attempts} attempts remaining to guess the number")
    guess = int(input("Make a guess: ")) #Gets user input on their guess and translate it to an int
    if guess == random_num: #If the user guesses correctly, then they win
        print(f"You got it! The answer was {random_num}")
        break #Breaks out of the loop, ending the game
    elif guess < random_num:
        print("Too low.\n Guess again.")
        attempts -= 1
    elif guess > random_num:
        attempts -= 1
        print("Too high. \n Guess again.")
    