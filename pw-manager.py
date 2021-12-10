import tkinter
import random
from tkinter import messagebox
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def ran_pas():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    b = ""
    c = ""
    j = ""
    nr_letters = 5
    nr_symbols = 5
    nr_numbers = 5
    for char in range(0, nr_letters):
        random_char = random.choice(letters)
        b = b + random_char
    for number in range(0, nr_numbers):
        g = random.randint(0, nr_numbers)
        c = c + numbers[g]
    for symbol in range(0, nr_symbols):
        r = random.randint(0, nr_symbols)
        j = j + symbols[r]
    password = ""
    passwword = b + c + j
    print(passwword)
    entry_pw.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_web.get()
    email = entry_em.get()
    password = entry_pw.get()
    new_data= {
        website:{
            "email":email,
            "password":password
        }
    }
    is_ok = messagebox.askokcancel(title="", message="Siguren si deka sakas da se zacuva?")
    if is_ok:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            data.update(new_data)
        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)



            entry_web.delete(0,"end")
            entry_pw.delete(0, "end")
# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password manager")
window.config(pady=20, padx=20)

photo = tkinter.PhotoImage(file="logo.png")

#Labels
web = tkinter.Label(text="Website:")
web.grid(column=0, row=1)
email = tkinter.Label(text="Email/Username:")
email.grid(column=0, row=2)
password = tkinter.Label(text="Password:")
password.grid(column=0, row=3)


#Canvas
canvas = tkinter.Canvas(width=200, height=200)
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

#Entry
entry_web = tkinter.Entry(width=35)
entry_web.grid(column=1, row=1)
entry_web.focus()
entry_em = tkinter.Entry(width=35)
entry_em.grid(column=1, row=2)
entry_pw = tkinter.Entry(width=35)
entry_pw.grid(column=1, row=3)


#Buttoms
pw_generator = tkinter.Button(width=15, text="Generate Password", command=ran_pas)
pw_generator.grid(column=3, row=3)
ad = tkinter.Button(width=30, text="Add", command=save)
ad.grid(column=1, row=4)


window.mainloop()