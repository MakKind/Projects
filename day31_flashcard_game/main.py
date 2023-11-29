from tkinter import *
import random

import pandas

try:
    Data = pandas.read_csv("data/words_to_learn.csv")
except (FileNotFoundError, pandas.errors.EmptyDataError):
    Data = pandas.read_csv("data/japanese_words.csv")
word_dict = Data.to_dict(orient='records')
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(word_dict)
    canvas_card.itemconfig(title, text="Japanese", fill='black')
    canvas_card.itemconfig(word, text=current_card["Japanese"], fill='black')
    canvas_card.itemconfig(card, image=front_img)
    flip_timer = window.after(3000, flip_card)


def is_known():
    word_dict.remove(current_card)
    data = pandas.DataFrame(word_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


def flip_card():
    canvas_card.itemconfig(title, text="English", fill='white')
    canvas_card.itemconfig(card, image=back_img)
    canvas_card.itemconfig(word, text=current_card["English"], fill='white')


BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

canvas_card = Canvas(width=800, height=526)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
card = canvas_card.create_image(400, 263, image=front_img)
title = canvas_card.create_text(400, 153, text="Japanese", font=("Ariel", 40, "italic"))
word = canvas_card.create_text(400, 263, text="Title", font=("Ariel", 50, "bold"))

canvas_card.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_card.grid(column=0, row=0, columnspan=2)

correct_img = PhotoImage(file="images/right.png")
button_correct = Button(image=correct_img, highlightthickness=0, command=is_known)
button_correct.grid(column=0, row=1)
wrong_img = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=wrong_img, highlightthickness=0, command=next_card)
button_wrong.grid(column=1, row=1)
next_card()
window.mainloop()
