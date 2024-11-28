from random import shuffle, randint, choice
from tkinter import *
from tkinter import messagebox

import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]

    shuffle(password_list)
    generated_password = "".join(password_list)

    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open('data.json', mode='r') as file:
            # Reading old data
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='No Data File Found')
    else:
        try:
            email = data[website]['email']
            password = data[website]['password']
        except KeyError as error:
            messagebox.showinfo(title='Error', message=f'No details for the website {error} exists.')
        else:
            messagebox.showinfo(title=f'{website}', message=f'Email: {email}\nPassword: {password}')


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_entry():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            'email': email,
            'password': password,
        }
    }

    if not website or not email or not password:
        messagebox.showinfo(title='Oops', message=f"Please make sure you haven't left any fields empty.")
    else:
        try:
            with open('data.json', mode='r') as file:
                # Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open('data.json', mode='w') as file:
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open('data.json', mode='w') as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

# Buttons
search_button = Button(width=14, text='Search', command=find_password)
search_button.grid(column=2, row=1)

password_button = Button(width=14, text='Generate Password', command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(width=35, text='Add', command=save_entry)
add_button.grid(column=1, row=4, columnspan=2)

# Entries
website_entry = Entry(width=20)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = Entry(width=40)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, 'patryk.glesman86@gmail.com')

password_entry = Entry(width=20)
password_entry.grid(column=1, row=3)

window.mainloop()
