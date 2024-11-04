# Code your name with NATO_alphabet

import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
dic_nato = {row.letter: row.code for (index, row) in df.iterrows()}


# Create a list of the phonetic code words from a word that the user inputs.
user_input = input("What is your name? ").upper()
user_code = [dic_nato[letter] for letter in user_input if letter in dic_nato]
print(user_code)

