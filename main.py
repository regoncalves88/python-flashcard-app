import pandas as pd
from random import choice
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
FONT_TITLE = ("Ariel", 40, "italic")
FONT_WORD = ("Ariel", 60, "bold")

portuguese_data = pd.read_csv("data/portuguese_words.csv")
data = portuguese_data.to_dict(orient="records")


def random_word():
    next_word = choice(data)
    canvas.itemconfig(card_title, text="Portuguese")
    canvas.itemconfig(card_word, text=next_word["Portuguese"])


window = Tk()
window.title("Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas_front_bg = PhotoImage(file="images/card_front.png")
canvas_back_bg = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.create_image(400, 263, image=canvas_front_bg)
card_title = canvas.create_text(400, 150, text="Title", font=FONT_TITLE)
card_word = canvas.create_text(400, 263, text="Word", font=FONT_WORD)
canvas.grid(column=0, row=0, columnspan=2)

unknown_button_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown_button_img, highlightthickness=0, command=random_word)
unknown_button.grid(column=0, row=1)

known_button_img = PhotoImage(file="images/right.png")
known_button = Button(image=known_button_img, highlightthickness=0, command=random_word)
known_button.grid(column=1, row=1)

random_word()

window.mainloop()
