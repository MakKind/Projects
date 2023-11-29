import random
from tkinter import *
from tkinter import messagebox
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    entry_password.delete(0, END)
    l = random.randint(12, 18)
    n = random.randint(2, 4)
    s = random.randint(2, 4)
    password_generated = []
    for i in range(l - n - s):
        if random.randint(1, 2) == 1:
            password_generated.append(chr(random.randint(65, 90)))
        else:
            password_generated.append(chr(random.randint(97, 122)))
    for i in range(n):
        password_generated.insert(random.randint(0, len(password_generated) - 1), str(random.randint(0, 9)))
    for i in range(s):
        if random.randint(1, 3) == 1:
            password_generated.insert(random.randint(0, len(password_generated) - 1), chr(random.randint(33, 47)))
        elif random.randint(1, 3) == 2:
            password_generated.insert(random.randint(0, len(password_generated) - 1), chr(random.randint(58, 64)))
        else:
            password_generated.insert(random.randint(0, len(password_generated) - 1), chr(random.randint(91, 96)))
    s = ("".join(password_generated))
    entry_password.insert(0, s)
    pyperclip.copy(s)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="ERROR!!", message="Please don't leave any fields empty.")
    else:
        try:
            with open("data.json", mode='r') as test:
                data = json.load(test)
                data.update(new_data)
        except (json.decoder.JSONDecodeError, FileNotFoundError):
            with open("data.json", mode='w') as test:
                json.dump(new_data, test, indent=4)
        else:
            with open("data.json", mode='w') as test:
                json.dump(data, test, indent=4)
        finally:
            entry_password.delete(0, END)
            entry_website.delete(0, END)


# ---------------------------- SEARCH ------------------------------- #
def search():
    search_word = entry_website.get()
    try:
        with open("data.json", mode='r') as test:
            data = json.load(test)
        email = data[search_word]["email"]
        password = data[search_word]["password"]
    except (json.decoder.JSONDecodeError, FileNotFoundError, KeyError):
        messagebox.showerror(title="ERROR", message=f"No details found for {search_word}")
    else:
        messagebox.showinfo(title=f"{search_word}", message=f"Email: {email}\nPasswprd: {password}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:", justify="left")
label_website.grid(column=0, row=1)
label_email = Label(text="Email/Username:", justify="left")
label_email.grid(column=0, row=2)
label_password = Label(text="Password:", justify="left")
label_password.grid(column=0, row=3)

entry_website = Entry(width=42)
entry_website.grid(column=1, row=1, columnspan=2)
entry_website.focus()
entry_email = Entry(width=42)
entry_email.insert(END, string="mainak@email.com")
entry_email.grid(column=1, row=2, columnspan=2)
entry_password = Entry(width=33)
entry_password.grid(column=1, row=3)

button_generate_pass = Button(text="Generate", command=generate_password)
button_generate_pass.grid(column=2, row=3)
button_add = Button(text="Add", width=36, command=save_password)
button_add.grid(column=1, row=4, columnspan=2)
button_search = Button(text="Search", command=search)
button_search.grid(column=2, row=1)

window.mainloop()
