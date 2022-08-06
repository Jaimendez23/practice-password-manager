from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

FONT_NAME = "Courier"


def saved_data():
    website = website_input.get()
    email = email_username_input.get()
    passwords = password_input.get()
    new_data = {website: {
        "email": email,
        "password": passwords
    }}

    if len(website) == 0 or len(passwords) == 0:
        messagebox.showinfo("Opppss", message="Please make sure you haven't left any fields empty")
    else:
        try:
            with open("password.json", "r") as data:
                # reading old data
                data_file = json.load(data)  # if print type return dictionary

        except FileNotFoundError:
            with open("password.json", "w") as data:
                # saving updated data
                json.dump(new_data, data, indent=4)
        else:
            # updating old data with new datas
            data_file.update(new_data)

            with open("password.json", "w") as data:
                # saving updated data
                json.dump(data_file, data, indent=4)
        finally:
            website_input.delete(0, "end")
            password_input.delete(0, "end")


def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


def search_info():
    website = website_input.get()
    try:
        with open("password.json") as data:
            data_file = json.load(data)  # data type is dictionary

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")

    else:
        if website in data_file:
            messagebox.showinfo(title=f"{website}", message=f"Email: {data_file[website]['email']}\n "
                                                            f"Password: {data_file[website]['password']}")
        else:
            messagebox.showinfo(title='Error', message=f"No details for {website} exists")


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_pic = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_pic)
canvas.grid(column=0, row=0, columnspan=3)

# <---------- labels ---------->
website_text = Label(text="Website:", font=(FONT_NAME, 12, "bold"))
website_text.grid(column=0, row=1)

email_username_text = Label(text="Email/Username:", font=(FONT_NAME, 12, "bold"))
email_username_text.grid(column=0, row=3)

password_text = Label(text="Password:", font=(FONT_NAME, 12, "bold"))
password_text.grid(column=0, row=4)

# <---------- entries ---------->
website_input = Entry(width=40)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_username_input = Entry(width=40)
email_username_input.grid(column=1, row=3, columnspan=2)
email_username_input.insert(0, "jaimendezofficial2@gmail.com")

password_input = Entry(width=40)
password_input.grid(column=1, row=4)

# <---------- Buttons ---------->
search_btn = Button(text="search", width=34, command=search_info)
search_btn.grid(column=1, row=2, columnspan=2)

generate_pass_btn = Button(text="Generate Password", width=34, command=generate_pass)
generate_pass_btn.grid(column=1, row=5, columnspan=1)

add_btn = Button(text="Add", width=34, command=saved_data)
add_btn.grid(column=1, row=6, columnspan=2)

window.mainloop()
