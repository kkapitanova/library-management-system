from database import *
import tkinter as tk

checkoutLbl = tk.Label(window, text="BOOK CHECKOUT",  font=("Arial Bold", 10), bg="#ffb8b8", fg="black")
checkoutLbl.grid(column=6, row=1)
checkoutLbl1 = tk.Label(window, text="Member ID:", bg="#ffb8b8")
checkoutLbl1.grid(column=5, row=2)
checkoutMemberID = tk.Entry(window, width=20)
checkoutMemberID.grid(column=6, row=2)
checkoutLbl2 = tk.Label(window, text="Book ID:", bg="#ffb8b8")
checkoutLbl2.grid(column=5, row=3)
checkoutBookID = tk.Entry(window, width=20)
checkoutBookID.grid(column=6, row=3)
checkoutResLbl = tk.Label(window, text="Results will appear here.", wraplength=150, bg="#ffb8b8", fg="black")
checkoutResLbl.grid(column=6, row=5)

logList = []  # empty list that will contain the the ID's of books and their corresponding checkout dates


def bookCheckout():
    try:
        bookID = checkoutBookID.get()  # gets book ID from user input
        memberID = checkoutMemberID.get()  # gets user ID
        if int(memberID) < 1000 or int(memberID) > 9999:
            checkoutResLbl.config(text="Sorry, the member ID you have entered is invalid.", fg="red")
        else:
            isvalid = validID(bookID)  # search the book ID in the database file
            if isvalid == bookID:  # checks whether bookID is valid and lets the program continue if it is
                searchResults = searchBookID(bookID)  # searches through the database file to get the book info
                if searchResults[4] == "0":
                    loanStatusToMemberID(memberID, bookID)
                    checkoutResLbl.config(text="The book was checked out successfully.", fg="green")
                    checkoutDateLog = getCheckoutDate(bookID)
                    return checkoutDateLog
                else:
                    checkoutResLbl.config(text="The book is currently on loan.", fg="red")
            else:
                checkoutResLbl.config(text="The book ID you have entered is not valid.\n"
                                           "Please try again.", fg="red")
    except:
        checkoutResLbl.config(text="An error has occurred.\n"
                                   "Please enter valid details.", fg="red")


if __name__ == "__main__":
    bookCheckout()