"""
An application to help the user with personal finance and financial literacy.
Amount, Type (spending/saving), Comment, Date(?)

The user can:

Labels:
See savings, spending, leftover revenue

Button (CONFIG):
Set currency
Set categories for spending
Set salary

Button (ADD):
Add monthly revenue
Add spending
Add ad-hoc revenue
Add savings

Button (MODIFY):
Adjust savings/spendings lines

BUTTON (NEW MONTH):
Create new month: revenue is renewed + rest of previous sent to savings

BUTTON (SEARCH):
Search for previous entries

BUTTON (DELETE):
Delete lines

BUTTON (CLOSE):
Close application

"""

# import everything from tkinter library
from tkinter import *

# tkinter instance
main_window = Tk()
main_window.title("Personal Finance")
main_window.geometry('1000x1000+50+50')

# labels and textbox
l1 = Label(main_window, text="Income", width=15)
l1.grid(row=0, column=0)

t1 = Text(main_window, height=1, width=15)
t1.grid(row=0, column=1)
t1.configure(state="disabled")

l2 = Label(main_window, text="Spending", width=15)
l2.grid(row=0, column=2)

t2 = Text(main_window, height=1, width=15)
t2.grid(row=0, column=3)
t2.configure(state="disabled")

l3 = Label(main_window, text="Left-over", width=15)
l3.grid(row=0, column=4)

t3 = Text(main_window, height=1, width=15)
t3.grid(row=0, column=5)
t3.configure(state="disabled")

l4 = Label(main_window, text="Savings", width=15)
l4.grid(row=0, column=6)

t4 = Text(main_window, height=1, width=15)
t4.grid(row=0, column=7)
t4.configure(state="disabled")

# listbox and scrollbar
list1 = Listbox(main_window, height=40, width=120)
list1.grid(row=1, column=0, rowspan=48, columnspan=6)

scroll1 = Scrollbar(main_window)
scroll1.grid(row=1, column=6, rowspan=48)

list1.configure(yscrollcommand=scroll1.set)
scroll1.configure(command=list1.yview)

# buttons
b1 = Button(main_window, text="Configure", width=10)
b1.grid(row=1, column=7)

b1 = Button(main_window, text="Add", width=10)
b1.grid(row=2, column=7)

b1 = Button(main_window, text="Modify", width=10)
b1.grid(row=3, column=7)

b1 = Button(main_window, text="Search", width=10)
b1.grid(row=4, column=7)

b1 = Button(main_window, text="New Month", width=10)
b1.grid(row=5, column=7)

b1 = Button(main_window, text="Delete", width=10)
b1.grid(row=6, column=7)

b1 = Button(main_window, text="Close", width=10)
b1.grid(row=7, column=7)

# keep window open
main_window.mainloop()