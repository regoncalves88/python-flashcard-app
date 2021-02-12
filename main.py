from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
FONT_TITLE = ("Ariel", 40, "italic")
FONT_WORD = ("Ariel", 60, "bold")

window = Tk()
window.title("Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas_front_bg = PhotoImage(file="images/card_front.png")
canvas_back_bg = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.create_image(400, 263, image=canvas_front_bg)
canvas.create_text(400, 150, text="Title", font=FONT_TITLE)
canvas.create_text(400, 263, text="Word", font=FONT_WORD)
canvas.grid(column=0, row=0, columnspan=2)

wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0)
wrong_button.grid(column=0, row=1)

right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0)
right_button.grid(column=1, row=1)

window.mainloop()
