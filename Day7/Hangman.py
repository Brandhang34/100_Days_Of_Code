#Step 3
import Hangman_art
import Hangman_words
import random

word_list = Hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

print(Hangman_art.logo)

#Create blanks
display = []
for _ in range(word_length):
    display += '_'

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
inprogress = True
life = 6

while(inprogress):
    guess = input("Guess a letter: ").lower()
    #Check guessed letter
    if guess in chosen_word:
        if guess in display:
            print(f"You've already guessed {guess}")
        else:
            for position in range(word_length):
                letter = chosen_word[position]
                #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
                if letter == guess:
                    display[position] = letter
    else:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        life -= 1
        if life <= 0:
            print(Hangman_art.stages[life])
            print("You Lose!")
            break
    if "_" not in display:
        print(Hangman_art.stages[life])
        print("You Win!")
        break
    print("Life: " + str(life))
    print(display)
    print(Hangman_art.stages[life])
