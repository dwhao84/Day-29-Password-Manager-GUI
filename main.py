import tkinter
from tkinter import *
from tkinter import Label
from tkinter import messagebox
import random
import pyperclip
import os

WEBSITE_LABEL_WIDTH = 35
PASSWORD_WIDTH = 21
ADD_BTN_WIDTH = 36

EMAIL = "dwsamurai84@gmail.com"

# ----- PASSWORD GENERATOR -----
def tapped_password_generator():
    print("pressed_password_generator")
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    # ( Section 1)
    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    # ( Section 2)
    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    password_list += [ random.choice(letters) for _ in range(nr_letters)]
    password_list += [ random.choice(letters) for _ in range(nr_symbols) ]
    password_list += [ random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = ""
    # for char in password_list:
    #     password += char
    password += ''.join(char for char in password_list)
    print(f"Your password is: {password}")
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ----- SAVE PASSWORD -----
def tapped_add_btn():
    print("tapped_save_password")

    # 找到 輸入框的內容。
    email_data = email_entry.get()
    password_data = password_entry.get()
    website_data = website_entry.get()

    if len(website_data) == 0 or len(password_data) == 0:
        print(f"Website:{ len(website_data) }, Password: { len(password_data) }")
        messagebox.showerror(title="Entry is empty", message=f"There are one of entry is empty: Website:{ len(website_data) }, password data: { len(password_data) }")
    else:
        is_ok = messagebox.askokcancel(title=website_data, message=f"There are the detail entered: \n Email: {email_data}"
                                                        f"\n Password: {password_data}, \n Is it ok to save?")
        if is_ok:
            DATASET = f'{email_data} | {password_data} | {website_data} \n'
            # 用with open的寫法 去撰寫dataset.txt。
            with open("dataset.txt", mode="a") as file:
                file.write(DATASET)
                print("dataset.txt wrote it.")

            # 用entry.delete()的方法，來清除輸入資料
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            print("Clean the Entry width.")

# ----- UI SETUP -----
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Move StringVar declarations here, after creating window
website = StringVar()
email = StringVar()
password_var = StringVar()  # Renamed to avoid conflict with Label

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)  # Changed from pack() to grid()

# Rest of your code with fixed row parameter and password variable name
website_label = Label(text="Website", fg="black", highlightthickness=0)
password_label = Label(text="Password", fg="black", highlightthickness=0)
email_label = Label(text="Email / User name", fg="black", highlightthickness=0)

website_label.grid(row=1, column=0, sticky='e')
email_label.grid(row=2, column=0, sticky='e')
password_label.grid(row=3, column=0, sticky='e')

# Change these grid() calls:
website_entry = Entry(width=WEBSITE_LABEL_WIDTH, textvariable=website)
website_entry.grid(row=1, column=1, columnspan=1, sticky='w')  # Added sticky='w'

email_entry = Entry(width=WEBSITE_LABEL_WIDTH, textvariable=email)
email_entry.grid(row=2, column=1, sticky='w')  # Added sticky='w'
email_entry.insert(0, EMAIL)

password_entry = Entry(width=PASSWORD_WIDTH, textvariable=password_var)
password_entry.grid(row=3, column=1, sticky='w')  # Added sticky='w'

generate_password_btn = Button(text="Generate Password", highlightthickness=0, command=tapped_password_generator)
generate_password_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=ADD_BTN_WIDTH, highlightthickness=0, command=tapped_add_btn)
add_btn.grid(row=4, column=1, columnspan=2, sticky='w')

window.mainloop()