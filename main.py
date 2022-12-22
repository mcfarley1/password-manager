from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- SEARCH WEBSITE ------------------------------- #
def search_website():
    def copy_password():
        password2 = password_entry2.get()
        pyperclip.copy(password2)
        messagebox.showinfo(title="Password", message="Your password has been copied to the clipboard "
                                                      "and is ready to paste.")
        password_entry2.focus()

    def update_info():
        update_name = username_entry2.get()
        update_pass = password_entry2.get()
        if len(update_name) == 0 or len(update_pass) == 0:
            messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty.")
            username_entry2.focus()
        else:
            data[website_upper]["username"] = update_name
            data[website_upper]["password"] = update_pass
            with open("data.json", "w") as data_file2:
                json.dump(data, data_file2, indent=4)
            messagebox.showinfo(title="Update", message="Your changes have been saved.")
            username_entry2.focus()

    def generate_password2():
        password_entry.delete(0, END)
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u',
                   'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                   'P',
                   'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
        letters_list = [choice(letters) for _ in range(randint(8, 10))]
        numbers_list = [choice(numbers) for _ in range(randint(2, 4))]
        symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
        password_list = letters_list + numbers_list + symbols_list
        shuffle(password_list)
        password2 = "".join(password_list)
        password_entry2.delete(0, END)
        password_entry2.insert(0, string=password2)

    website = website_entry.get()
    website_upper = website.upper()
    if len(website) == 0:
        messagebox.showinfo(title="Oops!", message="Please enter a website.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Oops!", message="There are no entries yet.")
        else:
            try:
                username = data[website_upper]["username"]
            except KeyError:
                messagebox.showinfo(title="Oops!", message=f"{website} not found.")
            else:
                password = data[website_upper]["password"]
                search_window = Toplevel(window)
                search_window.title(website_upper)
                search_window.config(padx=50, pady=50)
                username_label2 = Label(search_window, text="Email/Username:")
                username_label2.grid(column=0, row=0)
                password_label2 = Label(search_window, text="Password:")
                password_label2.grid(column=0, row=1)
                username_entry2 = Entry(search_window, width=51)
                username_entry2.insert(0, string=username)
                username_entry2.grid(column=1, row=0, columnspan=2, sticky="w")
                username_entry2.focus()
                password_entry2 = Entry(search_window, width=51)
                password_entry2.insert(0, string=password)
                password_entry2.grid(column=1, row=1, columnspan=2, sticky="w")
                copy_button = Button(search_window, text="Copy Password", width=14, command=copy_password)
                copy_button.grid(column=0, row=2, sticky="w")
                update_button = Button(search_window, text="Update Info", width=14, command=update_info)
                update_button.grid(column=1, row=2)
                new_pass_button = Button(search_window, text="New Password", width=14, command=generate_password2)
                new_pass_button.grid(column=2, row=2, sticky="w")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [choice(letters) for _ in range(randint(8, 10))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = letters_list + numbers_list + symbols_list

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, string=password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    website_upper = website.upper()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website_upper: {
            "username": username,
            "password": password,
        }
    }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
                pyperclip.copy(password)
                messagebox.showinfo(title="Password", message="Your password has been copied to the clipboard "
                                                              "and is ready to paste.")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
        else:
            try:
                data[website_upper]
            except KeyError:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
                pyperclip.copy(password)
                messagebox.showinfo(title="Password", message="Your password has been copied to the clipboard "
                                                              "and is ready to paste.")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
            else:
                messagebox.showinfo(title="Oops!", message="This entry already exists.")
                return


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry(width=32)
website_entry.grid(column=1, row=1, sticky="w")
website_entry.focus()
search_button = Button(text="Search", width=14, command=search_website)
search_button.grid(column=2, row=1, sticky="w")

username_entry = Entry(width=51)
username_entry.grid(column=1, row=2, columnspan=2, sticky="w")
password_entry = Entry(width=32)
password_entry.grid(column=1, row=3, sticky="w")

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3, sticky="w")
add_button = Button(text="Add", width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")


window.mainloop()
