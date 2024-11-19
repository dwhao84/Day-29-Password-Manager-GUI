from tkinter import *
from tkinter import Label

WEBSITE_LABEL_WIDTH = 35
PASSWORD_WIDTH = 21
ADD_BTN_WIDTH = 36


# ----- PASSWORD GENERATOR -----
def tapped_password_generator():
    print("pressed_password_generator")


# ----- SAVE PASSWORD -----
def tapped_save_password():
    print("tapped_save_password")


# ----- UI SETUP -----
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.pack()
canvas.grid(column=0, row=1)

website_label = Label(text="Website", fg="black", highlightthickness=0)
website_label.grid(column=0, rows=1)

email_label = Label(text="Email / Username", fg="black", highlightthickness=0)
email_label.grid(column=0, rows=1)

Password = Label(text="Password", fg="black", highlightthickness=0)
Password.grid(column=0, rows=2)

add_btn = Button(text="Add", highlightthickness=0, command=tapped_save_password)
add_btn.grid(column=2, rows=2)

generate_password_btn = Button(text="Generate Password", highlightthickness=0, command=tapped_password_generator)
generate_password_btn.grid(column=3, rows=2)
window.mainloop()
