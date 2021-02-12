import pandas as pd
from random import choice
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
FONT_TITLE = ("Ariel", 40, "italic")
FONT_WORD = ("Ariel", 60, "bold")

try:
    portuguese_data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    portuguese_data = pd.read_csv("data/portuguese_words.csv")
finally:
    words_to_learn = portuguese_data.to_dict(orient="records")

next_word = {}


def next_card():
    global next_word, flip_timer

    window.after_cancel(flip_timer)
    next_word = choice(words_to_learn)
    canvas.itemconfig(card_image, image=canvas_front_bg)
    canvas.itemconfig(card_title, text="Portuguese", fill="black")
    canvas.itemconfig(card_word, text=next_word["Portuguese"], fill="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_image, image=canvas_back_bg)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=next_word["English"], fill="white")


def is_known():
    words_to_learn.remove(next_word)
    data = pd.DataFrame(words_to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas_front_bg = PhotoImage(file="images/card_front.png")
canvas_back_bg = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_image = canvas.create_image(400, 263, image=canvas_front_bg)
card_title = canvas.create_text(400, 150, text="Title", font=FONT_TITLE)
card_word = canvas.create_text(400, 263, text="Word", font=FONT_WORD)
canvas.grid(column=0, row=0, columnspan=2)

unknown_button_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown_button_img, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

known_button_img = PhotoImage(file="images/right.png")
known_button = Button(image=known_button_img, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)

next_card()

window.mainloop()
