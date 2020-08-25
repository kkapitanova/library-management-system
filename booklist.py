import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from database import *

popularityLbl = tk.Label(window, text="BOOK POPULARITY", font=("Arial Bold", 10), bg="#ffb8b8")
popularityLbl.grid(column=8, row=1)

# the code below searches through the database to get the titles of the books
with open("database.txt", "r") as f:
    titles = []
    for line in f:
        lineList = line.replace("\n", "").split(",")
        if lineList[1] not in titles:
            titles.append(lineList[1])
    titles.remove("Title")


# the code below gets the number of times a book has been took on loan
with open("logfile.txt", "r") as fig:
    count1 = count2 = count3 = count4 = count5 = 0
    count6 = count7 = count8 = count9 = count10 = 0
    counters = [count1, count2, count3, count4, count5,
                count6, count7, count8, count9, count10]

    for line in fig:
        if titles[0] in line:
            count1 += 1
        if titles[1] in line:
            count2 += 1
        if titles[2] in line:
            count3 += 1
        if titles[3] in line:
            count4 += 1
        if titles[4] in line:
            count5 += 1
        if titles[5] in line:
            count6 += 1
        if titles[6] in line:
            count7 += 1
        if titles[7] in line:
            count8 += 1
        if titles[8] in line:
            count9 += 1
        if titles[9] in line:
            count10 += 1

fig = Figure(figsize=(16, 4), dpi=70)
ax = fig.add_subplot(111)

x = [titles[0], titles[1], titles[2], titles[3], titles[4],
     titles[5], titles[6], titles[7], titles[8], titles[9]]
y = [count1, count2, count3, count4, count5,
     count6, count7, count8, count9, count10]
width = .5

# x axis - name of the book
# y axis - number of times checked out

barGraph = ax.barh(x, y, width)
title = ax.set_title("Book Popularity")
title = ax.set_xlabel("Times Taken on Loan")
title = ax.set_ylabel("Title")

def popularity():
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().grid(column=8, row=6)


# for Testing
if __name__ == "__main__":
    popularity()
