from itertools import islice
from database import *
import tkinter as tk

searchLbl = tk.Label(window, text="BOOK SEARCH", font=("Arial Bold", 10), bg="#ffb8b8", fg="black")
searchLbl.grid(column=2, row=1)
searchLbl2 = tk.Label(window, text="Book Name:", bg="#ffb8b8")
searchLbl2.grid(column=1, row=2)
searchEntry = tk.Entry(window, width=20)
searchEntry.grid(column=2, row=2)
searchResLbl = tk.Label(window, text="Results will appear here.", wraplength=200, bg="#ffb8b8", fg="black")
searchResLbl.grid(column=2, row=4)


# the function below gives an output according the user's input in the search box
def searchResult():
    try:
        title = searchEntry.get()  # gets user input
        resultList = searchBookTitle(title)  # the function within the database module searches for the title

        if not resultList:  # if the book is not in the search file
            searchResLbl.config(text="Empty results.", fg="red")
        else:
            splitList = [list(islice(resultList, bookinfo))
                         for bookinfo in [5]]  # splits the original list into separate lists containing the book info
            resultString = ",".join(str(n) for splitList in resultList for n in splitList)  # turns list into string
            searchResLbl.config(text=resultString, fg="white")
    except:
        searchResLbl.config(text="Empty results.", fg="red")


# for Testing
if __name__ == "__main__":
    searchResult()