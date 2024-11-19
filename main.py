import tkinter
from tkinter import *
from tkinter import Label

WEBSITE_LABEL_WIDTH = 35
PASSWORD_WIDTH = 21
ADD_BTN_WIDTH = 36


# ----- PASSWORD GENERATOR -----
def tapped_password_generator():
    print("pressed_password_generator")


# ----- SAVE PASSWORD -----
def tapped_add_btn():
    print("tapped_save_password")
    # 把資料寫入dataset.txt裡面。
    with open("dataset.txt", mode="w") as file:
        file.write()


# ----- UI SETUP -----
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.pack()
canvas.grid(row=1, column=0)

# Labels
website_label = Label(text="Website", fg="black", highlightthickness=0)
website_label.grid(rows=1, column=0 )

email_label = Label(text="Email / User name", fg="black", highlightthickness=0)
email_label.grid(rows=2, column=0)

password = Label(text="Password", fg="black", highlightthickness=0)
password.grid(rows=3, column=0)

# Entry
website_entry = Entry(width=WEBSITE_LABEL_WIDTH)
website_entry.grid(rows=1, column=1, columnspan=)

# email entry
email_entry = Entry(width=WEBSITE_LABEL_WIDTH)
email_entry.grid(rows=2, column=1)

# password entry
password_entry = Entry(width=PASSWORD_WIDTH)
password_entry.grid(rows=3, column=1)

generate_password_btn = Button(text="Generate Password", highlightthickness=0, command=tapped_password_generator)
generate_password_btn.grid(rows=3, column=2)

add_btn = Button(text="Add", highlightthickness=0, command=tapped_add_btn)
add_btn.grid(rows=4, column=1)

window.mainloop()
