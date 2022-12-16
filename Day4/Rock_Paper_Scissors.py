import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

computer = random.randint(0,2)

hand=[rock, paper, scissors]

print(hand[player] + "\n")

print("Computer chose: \n" + hand[computer])

if player == computer:
    print("Tie Game")
elif player == 0 and computer == 1 or player == 1 and computer == 2 or player == 2 and computer == 0:
    print("You Lose")
else:
    print("You Win")