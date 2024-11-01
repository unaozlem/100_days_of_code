# HANGMAN GAME

import random
import hangman_words
import hangman_art

# Choose a random word from hangman_words.py
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Hangman logo added
print(hangman_art.logo)

# To test the solution
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = ["_" for _ in range(word_length)]
guessed_letters = []  # To keep track of all guessed letters

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Check if the user has already guessed the letter
    if guess in guessed_letters:
        print(f"You have already guessed '{guess}'. Try a different letter.")
        continue

    # Add the current guess to the guessed letters list
    guessed_letters.append(guess)

    # Check guessed letter and update display if the letter is in chosen_word
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Check if user is wrong
    if guess not in chosen_word:
        print(f"You guessed '{guess}', which is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word was: {chosen_word}")

    # Display current progress
    print(f"{' '.join(display)}")

    # Check if user has completed the word
    if "_" not in display:
        end_of_game = True
        print("You win!")

    # Display hangman stages based on lives left
    print(hangman_art.stages[lives])
