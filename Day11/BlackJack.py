############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

import art
import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Function that deals a random card
def deal_card(lst_of_cards):
    return lst_of_cards.append(random.choice(cards))

#Function that prints the hand of the players card
def print_cards():
    print(f"     Your cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"     Computer's first card: {computer_cards[0]}")

#Function that checks if either the player or the computer has won and prints the final score.
def end_game_checker():
    final_user_score = sum(user_cards)
    final_computer_score = sum(computer_cards)

    print(f"     Your final hand: {user_cards}, final score: {final_user_score}")
    print(f"     Computer's final hand: {computer_cards}, final score: {final_computer_score}")
    if final_user_score > 21: print("You went over. You Lose.")
    elif final_computer_score > 21: print("Computer went over. You Win.")
    elif final_user_score < 21 and final_computer_score < final_user_score: print("You win!")
    elif final_user_score == final_computer_score: print("Draw!")
    elif final_computer_score < 21 and final_computer_score > final_user_score: print("Computer wins!")
    elif final_user_score == 21: print("You win with a black jack.")
    elif final_computer_score == 21: print("Computer wins with a black jack.")



ongoing_game = True  #Checks if the game is ongoing
while(ongoing_game):
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':   
        os.system('cls' if os.name == 'nt' else 'clear') #clears the terminal
        print(art.logo)

        #Create an empty list
        user_cards = []
        computer_cards = []

        #Deal both users and computer a starting hand of 2 card values
        for i in range(0,2):
            deal_card(user_cards)
            deal_card(computer_cards)

        #print the 2 random cards given to the user and computers first card
        print_cards()

        #Detect when computer or user has a blackjack. (Ace + 10 value card).
        if sum(user_cards) == 21 or sum(computer_cards) == 21:
            end_game_checker()
        else: 
            keep_drawing = True
            while keep_drawing:
                if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
                    deal_card(user_cards) #calls the function if the user wants to keep drawing a card
                    if sum(user_cards) == 21 or sum(user_cards) > 21:
                        keep_drawing = False
                    print_cards()
                else:
                    while sum(computer_cards) < 16: #loops and draws a random card until the sum of the computer cards is less than 16
                        deal_card(computer_cards)
                    keep_drawing = False
            end_game_checker()
    else:
        #Whether if the user wants to play again.
        ongoing_game = False