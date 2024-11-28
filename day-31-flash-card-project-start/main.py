from tkinter import *
from random import choice
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ('Ariel', 40, 'italic')
WORD_FONT = ('Ariel', 60, 'bold')

random_fw: dict | None = None

try:
    fw_csv = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    fw_csv_org = pd.read_csv('data/french_words.csv')
    fw_dict = pd.DataFrame(fw_csv_org).to_dict(orient='records')
else:
    fw_dict = pd.DataFrame(fw_csv).to_dict(orient='records')


# ---------------------------- CHECK/WRONG ------------------------------- #
def check():
    global random_fw

    if len(fw_dict) > 1:
        fw_dict.remove(random_fw)
        pd.DataFrame(fw_dict).to_csv('data/words_to_learn.csv', index=False)
    french_word()


# ---------------------------- FRENCH CARD GENERATOR ------------------------------- #
def french_word():
    global timer
    global random_fw

    window.after_cancel(timer)
    random_fw = choice(fw_dict)
    canvas.itemconfig(word, text=random_fw['French'], fill='black')
    canvas.itemconfig(language, text='French', fill='black')
    canvas.itemconfig(canvas_image, image=front_card_img)

    timer = window.after(3000, english_word)


def english_word():
    global random_fw

    canvas.itemconfig(word, text=random_fw['English'], fill='white')
    canvas.itemconfig(language, text='English', fill='white')
    canvas.itemconfig(canvas_image, image=back_card_img)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(3000, english_word)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_img = PhotoImage(file='images/card_front.png')
back_card_img = PhotoImage(file='images/card_back.png')
canvas_image = canvas.create_image(405, 273, image=front_card_img)
canvas.grid(column=0, row=0, columnspan=2)
language = canvas.create_text(400, 150,  text='', font=LANGUAGE_FONT)
word = canvas.create_text(400, 263,  text='', font=WORD_FONT)

# Buttons
wrong_image = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=french_word)
wrong_button.grid(column=0, row=2)

right_image = PhotoImage(file='images/right.png')
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=check)
right_button.grid(column=1, row=2)

french_word()

window.mainloop()
