from bookcheckout import *
from booklist import *
from database import *
import tkinter as tk

returnLbl = tk.Label(window, text="BOOK RETURN", font=("Arial Bold", 10), bg="#ffb8b8", fg="black")
returnLbl.grid(column=4, row=1)
returnLbl2 = tk.Label(window, text="Book ID:", bg="#ffb8b8", fg="black")
returnLbl2.grid(column=3, row=2)
returnEntry = tk.Entry(window, width=20)
returnEntry.grid(column=4, row=2)
retResultLbl = tk.Label(window, text="Results will appear here.", wraplength=150, bg="#ffb8b8", fg="black")
retResultLbl.grid(column=4, row=4)


# the function has an output depending on the book that is wished to be returned
def bookReturn():
    try:
        bookID = returnEntry.get()  # gets book ID from user input
        isvalid = validID(bookID)  # search the book ID in the database file
        if isvalid == bookID:  # checks whether bookID is valid and lets the program continue if it is
            searchResults = searchBookID(bookID)  # searches through the database file to get the book info
            if searchResults[4] == "0":
                retResultLbl.config(text="The book is already available.", fg="red")
            else:
                loanStatusNull(bookID)
                getReturnDate(getCheckoutDate(bookID))
                retResultLbl.config(text="The book has been successfully returned.", fg="green")
        else:
            retResultLbl.config(text="The book ID you have entered is not valid.\n"
                                     "Please try again.", fg="red")
    except:
        retResultLbl.config(text="An error has occurred.\n"
                                 "Please enter valid details.", fg="red")


# for Testing
if __name__ == "__main__":
    bookReturn()