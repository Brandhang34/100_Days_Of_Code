import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)
user_continue = True
while(user_continue):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    def caesar(text, shift, direction):
        end_text = ''
        if direction == 'encode':
            for letter in text:
                if letter in alphabet:
                    end_text += alphabet[alphabet.index(letter) + shift]
                else:
                    end_text += letter
            print(f"The encoded text is: {end_text}")
        else:
            for letter in text:
                end_text += alphabet[alphabet.index(letter) - shift]
            print(f"The decoded text is: {end_text}")

    shift = shift % 26

    caesar(text,shift,direction)
    user_restart = input("Type 'yes' if you want to go again. Other wise type 'no'.\n")
    if user_restart == 'no':
        user_continue=False
        print("Goodbye")