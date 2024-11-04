from tkinter import *
from tkinter import messagebox
import random

LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
SYMBOLS = '!#$%^&*_-+=|\:;<>.?/'

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_gen():
    password_list = []
    for _ in range (10):
        number=str(random.randint(0, 9))
        char=random.choice(LETTERS)
        symbol = random.choice(SYMBOLS)
        password_list.append(random.choice([number, char, symbol]))

    password = ''.join(password_list)
    password_input.insert(0, password)
    return password

# ---------------------------- ALTERNATIVE PASSWORD GENERATOR ------------------------------- #

# from random import randint, shuffle, choice

# def password_gen():
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#     char = [choice(letters) for _ in range(randint(8, 10))]
#     sym = [choice(symbols) for _ in range(randint(2, 4))]
#     num = [choice(numbers) for _ in range(randint(2, 4))]

#     password_list = char + sym + num
#     shuffle(password_list)
#     password = ''.join(password_list)
#     password_input.insert(0, password)
#     print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_info = web_input.get()
    email_info = email_input.get()
    password_info = password_gen()
    line = website_info + " " + "|" + " " + email_info + " " + "|" + " " + password_info

    if len(website_info) == 0 or len(password_info) == 0:
        messagebox.showwarning("Warning", "Please don't leave any space empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_info, 
                            message=f"These are the information you have entered: \n Website:{website_info} \n E-mail: {email_info} \n Password:{password_info} \n Are they ok to save?")
        if is_ok:
            with open('password_data.txt', 'a') as f:
                f.write(f"{line}\n")
                web_input.delete(0, END)
                password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
my_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=my_img)
canvas.grid(column=1, row=0)

# Inputs
web_input = Entry(width=38)
web_input.grid(column=1, row=1, columnspan=2)
web_input.focus()

email_input = Entry(width=38)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "ozlem@gmail.com")

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Buttons
generate_button = Button(text="Generate Password", command=password_gen) 
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()