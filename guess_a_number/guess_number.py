#Number Guessing Game Objectives:


from random import randint
from art_guess_number import logo
print(logo)

# Allow the player to submit a guess for a number between 1 and 100.
number = randint(1,100)

# Offer two difficulty level to the player (10 guesses in easy mode, only 5 guesses in hard mode).
difficulty_level = input("Choose a difficulty level. 'Easy' or 'Hard': ").lower()
left_attempts_easy = 10
left_attempts_hard = 5


# If they run out of turns, provide feedback to the player. 
def asses_guess():
    if guess > number:
        print(f"{guess} too high!")
    elif guess < number:
        print(f"{guess} too low!")
    else:
        print(f"{guess} is not a valid number.")
    

is_continue = True
while is_continue:
    guess = int(input("Guess a number between 1 and 100: "))
    if  guess == number:
        print(f"Correct! You got it! It was {number}")
        is_continue = False
    elif difficulty_level == "easy" and left_attempts_easy > 0:
        asses_guess()
        left_attempts_easy -= 1
        print(f"You have {left_attempts_easy} attempts remaining to guess the number")
    elif difficulty_level == "hard" and left_attempts_hard > 0:
        asses_guess()
        left_attempts_hard -= 1
        print(f"You have {left_attempts_hard} attempts remaining to guess the number")
    else:
        is_continue = False
        print("You lost. No remaining attempts.")
