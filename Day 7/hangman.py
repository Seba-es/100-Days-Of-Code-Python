import random
from replit import clear
from hangman_words_list import word_list
from hangman_art import logo, stages


chosen_word = random.choice(word_list)
game = True
lives = 6
print(logo)

# Create blanks
display = ["_"]
for i in range(1, len(chosen_word)):
    display += "_"

while game:
    guess = input("Guess a letter: ").lower()
    clear()
    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")
    count = 0
    # Check guessed letter
    for letter in chosen_word:
        count += 1
        if letter == guess:
            display[count - 1] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        print(f"You have {lives} left")
        if lives == 0:
            game = False
            print("You lose.")
            print(f'The word was "{chosen_word}"')

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        game = False
        print("You win.")
    print(stages[lives])
