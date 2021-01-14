
#Creating a password generator

import random
from tkinter import *
import string

#Creating the password generator

def generate_password():
    password=[]
    for i in range(6):
        alpha = random.choice(string.ascii_letters)
        symbol = random.choice(string.punctuation)
        number = random.choice(string.digits)
        password.append(alpha)
        password.append(symbol)
        password.append(number)

    y = "".join(str(x) for x in password)
    lbl.config(text=y)

#creating the GUI

window = Tk()
window.title("Password Generator App")
window.geometry("300x150")
lbl = Label(window, text="Hello!",font=("Arial Bold",15,"bold"))
lbl.grid(row=0,column=0)
btn = Button(window, text="Generate Password",bg="green", fg="white",command=generate_password)
btn.grid(row=2,column=2)
window.mainloop()