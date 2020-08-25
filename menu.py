# Intro To Programming Coursework
# Written by Kristina Kapitanova
# Student ID: B917186
# Dec. 12th, 2019

import tkinter as tk
from database import *
from bookcheckout import *
from booksearch import *
from bookreturn import *
from booklist import *

window.title("Library Management System")
window.geometry("1800x900")


searchBtn = tk.Button(window, text="Search", bg="#58B19F", fg="white", command=searchResult)
searchBtn.grid(column=2, row=3)

returnBtn = tk.Button(window, text="Return", bg="#58B19F", fg="white", command=bookReturn)
returnBtn.grid(column=4, row=3)

checkoutBtn = tk.Button(window, text="Check out", bg="#58B19F", fg="white", command=bookCheckout)
checkoutBtn.grid(column=6, row=4)

popularityBtn = tk.Button(window, text="Show Book Popularity", bg="#58B19F", fg="white", command=popularity)
popularityBtn.grid(column=8, row=2)

window.mainloop()


