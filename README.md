# library-management-system

# MENU:
The menu gives the user access to all of the functions the program has to offer.
In order to run the whole program, the user must run menu.py.

# BOOK SEARCH:
This is a function that allows the user to search for a book, based on its title, by entering its name in the entry box.
The button bellow the entry box will activate the program's search function which will return all of the books and their information that correspond to the user input.
If the user searches for a book by any of its other attributes (i.e. Author, ID, etc.) the program will show empty results.

# BOOK CHECKOUT:
This is a function that allows the user to check out a book by entering the user's member ID and the book's ID in the corresponding entry boxes.
The program searches through the database, finds the book that the user wants to check out and changes the availability of the checked out book.
This means that the program changes the book's loan status number from '0' to the user's ID to indicate that that particular user has the book.
The valid ID's are 4-digit integers (1000-9999).
If the user enters either an invalid member ID or an invalid book ID, the program will show an error message and ask the user to enter correct details.
If the book is already checked out by someone else, the program will return a message stating that the book the user wants is already on loan and will ask the user to try again.

# BOOK RETURN:
This is a function that allows the user to return any book that has been checked out by them by entering the book ID in the entry box.
The program, similarly to the book checkout procedure, will run through the database and find the book that is wished to be returned.
It checks whether the book is on loan and if so, updates the database by changing the loan status from the borrower's member ID to '0', indicating that the book is free to loan.
If the book's loan status is 0, the program will show a message that the book is already available and will ask the user to try again.
The logfile updates upon the return of a book.

# BOOK POPULARITY:
This is a function that creates a graph showing the book popularity based on how many times a title has been taken on loan.
The program runs through the database to get the titles of all books that the library has to offer.
It then runs through the log to get the number of times each book has been checked out.
The program takes into consideration that different copies of the same book have different IDs.

# DATABASE.TXT
This file stores all of the books available at the library with their information in such an order:
ID,Title,Author,Year Published,Loan Status
If the Loan Status is '0' this means the book is available for loan.
Otherwise, the Loan Status will contain the borrower's member ID.

# LOG.TXT:
This file stores all data about the books that have been loaned in such an order:
BookID,Checkout Date,Return Date,Title
