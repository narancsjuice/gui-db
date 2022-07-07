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
import backend

# tkinter instance
main_window = Tk()
main_window.title("Personal Finance")
main_window.geometry('1000x1000+50+50')


def open_config():
    config_window = Toplevel(main_window)
    config_window.title("Configuration")
    cl1 = Label(config_window, text="Current config")
    cl1.grid(row=0, column=1)
    clb1 = Listbox(config_window, height=1, width=64)
    clb1.grid(row=1, column=1, columnspan=3)
    cl2 = Label(config_window, text="New config")
    cl2.grid(row=2, column=1)
    ce1_value = StringVar()
    ce2_value = StringVar()
    ce3_value = IntVar()
    #TODO: add default or labels for entry textboxes
    ce1 = Entry(config_window, textvariable=ce1_value)
    ce2 = Entry(config_window, textvariable=ce2_value)
    ce3 = Entry(config_window, textvariable=ce3_value)
    ce1.grid(row=3, column=1)
    ce2.grid(row=3, column=2)
    ce3.grid(row=3, column=3)
    cb1 = Button(config_window, text="Update config", width=10)
    cb1.grid(row=4, column=1)
    cb2 = Button(config_window, text="Close", width=10, command=config_window.destroy)
    cb2.grid(row=4, column=2)
    #TODO: opening new windows closes previous ones OR does not let you open new ones


def open_addline():
    add_window = Toplevel(main_window)
    add_window.title("Add New Line")
    ae1_value = DoubleVar()
    ae2_value = IntVar()
    ae3_value = StringVar()
    ae1 = Entry(add_window, textvariable=ae1_value)
    ae2 = Entry(add_window, textvariable=ae2_value)
    ae3 = Entry(add_window, textvariable=ae3_value)
    al1 = Label(add_window, text="Amount")
    al2 = Label(add_window, text="Category")
    al3 = Label(add_window, text="Description")
    ae1.grid(row=1, column=1)
    ae2.grid(row=1, column=2)
    ae3.grid(row=1, column=3)
    al1.grid(row=0, column=1)
    al2.grid(row=0, column=2)
    al3.grid(row=0, column=3)
    ab1 = Button(add_window, text="Search", width=10)
    ab1.grid(row=4, column=1)
    ab2 = Button(add_window, text="Close", width=10, command=add_window.destroy)
    ab2.grid(row=4, column=2)


def open_modifyline():
    modify_window = Toplevel(main_window)
    modify_window.title("Modify Line")
    me1_value = DoubleVar()
    me2_value = IntVar()
    me3_value = StringVar()
    me1 = Entry(modify_window, textvariable=me1_value)
    me2 = Entry(modify_window, textvariable=me2_value)
    me3 = Entry(modify_window, textvariable=me3_value)
    ml1 = Label(modify_window, text="Amount")
    ml2 = Label(modify_window, text="Category")
    ml3 = Label(modify_window, text="Description")
    me1.grid(row=1, column=1)
    me2.grid(row=1, column=2)
    me3.grid(row=1, column=3)
    ml1.grid(row=0, column=1)
    ml2.grid(row=0, column=2)
    ml3.grid(row=0, column=3)
    mb1 = Button(modify_window, text="Modify", width=10)
    mb1.grid(row=4, column=1)
    mb2 = Button(modify_window, text="Close", width=10, command=modify_window.destroy)
    mb2.grid(row=4, column=2)


def open_search():
    search_window = Toplevel(main_window)
    search_window.title("Search")
    se1_value = DoubleVar()
    se2_value = IntVar()
    se3_value = StringVar()
    se1 = Entry(search_window, textvariable=se1_value)
    se2 = Entry(search_window, textvariable=se2_value)
    se3 = Entry(search_window, textvariable=se3_value)
    sl1 = Label(search_window, text="Amount")
    sl2 = Label(search_window, text="Category")
    sl3 = Label(search_window, text="Description")
    se1.grid(row=1, column=1)
    se2.grid(row=1, column=2)
    se3.grid(row=1, column=3)
    sl1.grid(row=0, column=1)
    sl2.grid(row=0, column=2)
    sl3.grid(row=0, column=3)
    sb1 = Button(search_window, text="Search", width=10)
    sb1.grid(row=4, column=1)
    sb2 = Button(search_window, text="Close", width=10, command=search_window.destroy)
    sb2.grid(row=4, column=2)


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

#TODO: better listbox with columns

# listbox and scrollbar
list1 = Listbox(main_window, height=40, width=120)
list1.grid(row=1, column=0, rowspan=48, columnspan=6)

# load list items
for row in backend.view():
    list1.insert(END, row)

scroll1 = Scrollbar(main_window)
scroll1.grid(row=1, column=6, rowspan=48)

list1.configure(yscrollcommand=scroll1.set)
scroll1.configure(command=list1.yview)

# buttons
b1 = Button(main_window, text="Configure", width=10, command=open_config)
b1.grid(row=1, column=7)

b2 = Button(main_window, text="Add", width=10, command=open_addline)
b2.grid(row=2, column=7)

b3 = Button(main_window, text="Modify", width=10, command=open_modifyline)
b3.grid(row=3, column=7)

b4 = Button(main_window, text="Search", width=10, command=open_search)
b4.grid(row=4, column=7)

b5 = Button(main_window, text="New Month", width=10)
b5.grid(row=5, column=7)

b6 = Button(main_window, text="Delete", width=10)
b6.grid(row=6, column=7)

b7 = Button(main_window, text="Close", width=10, command=main_window.destroy)
b7.grid(row=7, column=7)

#TODO: refresh button for list items?
#def view_command():
    #list1.delete(0,END)
    #for row in backend.view():
        #list1.insert(END, row)
#8 = Button(main_window, text="Refresh", width=10)
#8.grid(row=8, column=7)

# keep window open
main_window.mainloop()