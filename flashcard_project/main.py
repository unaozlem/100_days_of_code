# Learn French with Flash Cards

from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
data_dict = {}

try:
    df_to_learn = pd.read_csv("./data/french_words.csv")
except FileNotFoundError:
    df_original = pd.read_csv("./data/french_words.csv")
    data_dict = df_original.to_dict(orient="records")
else:
    data_dict = df_to_learn.to_dict(orient="records")

#------------------ Delete Words From Database ---------------
def is_known():
    data_dict.remove(current_card)
    print(len(data_dict))
    data = pd.DataFrame(data_dict)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


#------------------------- Choose Random Word ----------------
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    current_fr_word = current_card['French']
    canvas.itemconfig(language_text, text = "French", fill="black")
    canvas.itemconfig(word_text, text=current_fr_word, fill="black")
    canvas.itemconfig(canvas_image, image = front_image)
    flip_timer = window.after(3000, func=flip_card)


#------------------------- Flip The Card ---------------------
def flip_card():
    current_en_word = current_card['English']
    canvas.itemconfig(language_text, text = "English", fill="white")
    canvas.itemconfig(word_text, text=current_en_word, fill="white")
    canvas.itemconfig(canvas_image, image = back_image)


#------------------------- User Interface --------------------
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

back_image = PhotoImage(file= "./images/card_back.png")
front_image = PhotoImage(file= "./images/card_front.png")
right_image = PhotoImage(file= "./images/right.png")
wrong_image = PhotoImage(file= "./images/wrong.png")


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=front_image)
language_text = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)



next_card()

window.mainloop()