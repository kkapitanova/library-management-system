import tkinter as tk
from datetime import date

window = tk.Tk()
window.configure(bg='#ffb8b8')


# the function below checks whether the book ID input by the user is valid
def validID(bookID):
    with open("database.txt", "r") as f:
        for line in f:  # loops through each line in the file
            lineList = line.replace("\n", "").split(",")  # creates a list of each line
            if bookID in lineList[0]:  # searches whether the book ID is in the list above
                return bookID  # returns book ID if it finds a match


# the function below returns the name of the book that corresponds to a certain ID number
# to be used when updating the log file
def getBookName(bookID):
    bookName = searchBookID(bookID)[1]
    return bookName


# the function below searches for a book by its title and
# returns the book information if it finds a match
def searchBookTitle(title):
    bookList = []  # a list where all data will be stored
    f = open("database.txt", "r")
    for line in f:
        lineList = line.replace("\n", "").split(",")  # turns each line of the text file into a list
        if title == lineList[1]:  # checks whether the title is in the corresponding line of the file
            bookList.append(lineList)
    return bookList  # returns the line that corresponds to the title


# the function below searches for a book by its ID and 
# returns the book information if it finds a match
def searchBookID(bookID):
    bookList = []  # a list where all data will be stored
    with open("database.txt", "r") as f:
        for line in f:
            lineList = line.replace("\n", "").split(",")  # turns each line into a list
            if bookID in lineList[0]:  # checks whether the title is in the corresponding line of the file
                bookList.append(lineList)
    return bookList[0]  # returns the line with information that corresponds to the title


# the function below takes the book ID and searches the database to find a match
# when it finds a match it returns the number of the line that contains the information
# the line number will be used when overwriting the data in the "database.txt" file
def bookIDIndex(bookID):
    with open("database.txt", "r") as f:
        bookList = []  # list that stores all data
        bookLine = []  # list that contains the book information
        for line in f:
            lineList = line.replace("\n", "").split(",")  # creates a list of each line
            bookList.append(lineList)
            if bookID in line:
                line = line.replace("\n", "").split(",")  # creates a list of the selected line
                bookLine.append(line)  # appends the line that contains the book info
                lineIndex = bookList.index(bookLine[0])
                # gets the index of the element in the list that contains the book information
                # index to be used when overwriting the information about a book
        return lineIndex


# the function below rewrites the loan status of the book when it is returned or checked out
def loanStatusNull(bookID):
    bookList = []  # a list where all data will be stored
    with open("database.txt", "r") as f:
        for line in f:
            lineList = line.replace("\n", "").split(",")
            bookList.append(lineList)
            lineOfBook = bookIDIndex(bookID)
    bookList[lineOfBook][4] = "0"  # rewrites the loan status to 0, meaning the book is available to loan
    with open("database.txt", "w") as newf:
        for bookID in bookList:
            newf.write(",".join(bookID))  # writes the data into the database file
            newf.write("\n")  # inserts a new line after the end of each line containing info for a certain book
        newf.close()


# the function below updates the loan status of a book
# to be used during checkout procedure
def loanStatusToMemberID(memberID, bookID):
    bookList = []  # a list where all data will be stored
    with open("database.txt", "r") as f:
        for line in f:
            lineList = line.replace("\n", "").split(",")  # turns each line into a list
            bookList.append(lineList)
            lineOfBook = bookIDIndex(bookID)  # rewrites loan status to the member ID of the borrower
    bookList[lineOfBook][4] = memberID  # rewrites the loan status to 0, meaning the book is available to loan
    with open("database.txt", "w") as newf:
        for bookID in bookList:
            newf.write(",".join(bookID))  # writes the data into the database file
            newf.write("\n")  # inserts a new line after the end of each line containing info for a certain book
        newf.close()


# this function generates the checkout date
# it also stores the new log into the logfile with the book ID and checkout date
def getCheckoutDate(bookID):
    today = date.today()  # gets today's date
    checkoutDate = today.strftime("%d/%m/%y")  # formats the date and time to d/m/y format
    halfLogString = (bookID + "," + checkoutDate)
    return halfLogString


# this function generates the return date
# it also updates the already existing log in the logfile with the return date and book name
def getReturnDate(halfLogString):
    logList1 = []  # a list where all the data is stored
    with open("logfile.txt", "r") as f:
        for line in f:
            lineList = line.replace("\n", "").split(",")  # makes each line of the data a separate list
            logList1.append(lineList)  # adds the data in one big list
        halfList = halfLogString.split(",")
        logList1.append(halfList)

    if halfList in logList1:
        bookName = getBookName(halfList[0])  # get the name of the book
        today = date.today()  # gets today's date
        returnDate = today.strftime("%d/%m/%y")  # formats the date in ddd/mmm/yyy format
        fullLog = ("\n" + halfLogString + "," + returnDate + "," + bookName)
        with open("logfile.txt", "a+") as lf:
            lf.write(fullLog)  # updates the logfile by adding return date
            lf.close()


# For testing - Search Title
if __name__ == '__main__':
    title = "The Great Gatsby"
    searchBookTitle(title)

# For testing - Search for a Book by its ID
if __name__ == '__main__':
    bookID = "426"
    searchBookID(bookID)

# For testing - Book Checkout
if __name__ == '__main__':
    memberID = "1423"
    bookID = "426"
    loanStatusToMemberID(memberID, bookID)

# For testing - Book Return
if __name__ == '__main__':
    bookID = "426"
    loanStatusNull(bookID)

# For testing - Get Return Date
if __name__ == '__main__':
    halfLogString = "633,Hamlet"
    getReturnDate(halfLogString)

# For testing - Get Checkout Date
if __name__ == '__main__':
    bookID = "1232"
    getCheckoutDate(bookID)

# For testing - Get Book Name
    bookID = "633"
    getBookName(bookID)
