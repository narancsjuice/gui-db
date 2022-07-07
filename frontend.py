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
class App(Tk):
    def __init__(self):
        super().__init__()

        self.geometry('1000x1000+50+50')
        self.title("Personal Finance")

        # labels and textbox
        self.l1 = Label(self, text="Income", width=15)
        self.l1.grid(row=0, column=0)
        self.t1 = Text(self, height=1, width=15)
        self.t1.grid(row=0, column=1)
        self.t1.configure(state="disabled")
        self.l2 = Label(self, text="Spending", width=15)
        self.l2.grid(row=0, column=2)
        self.t2 = Text(self, height=1, width=15)
        self.t2.grid(row=0, column=3)
        self.t2.configure(state="disabled")
        self.l3 = Label(self, text="Left-over", width=15)
        self.l3.grid(row=0, column=4)
        self.t3 = Text(self, height=1, width=15)
        self.t3.grid(row=0, column=5)
        self.t3.configure(state="disabled")
        self.l4 = Label(self, text="Savings", width=15)
        self.l4.grid(row=0, column=6)
        self.t4 = Text(self, height=1, width=15)
        self.t4.grid(row=0, column=7)
        self.t4.configure(state="disabled")

        # TODO: better listbox with columns

        # listbox and scrollbar
        self.list1 = Listbox(self, height=40, width=120)
        self.list1.grid(row=1, column=0, rowspan=48, columnspan=6)

        # load list items
        for row in backend.view():
            self.list1.insert(END, row)

        self.scroll1 = Scrollbar(self)
        self.scroll1.grid(row=1, column=6, rowspan=48)

        self.list1.configure(yscrollcommand=self.scroll1.set)
        self.scroll1.configure(command=self.list1.yview)

        # buttons
        self.b1 = Button(self, text="Configure", width=10, command=self.open_config)
        self.b1.grid(row=1, column=7)
        self.b2 = Button(self, text="Add", width=10, command=self.open_addline)
        self.b2.grid(row=2, column=7)
        self.b3 = Button(self, text="Modify", width=10, command=self.open_modifyline)
        self.b3.grid(row=3, column=7)
        self.b4 = Button(self, text="Search", width=10, command=self.open_search)
        self.b4.grid(row=4, column=7)
        self.b5 = Button(self, text="Refresh", width=10, command=self.refresh)
        self.b5.grid(row=5, column=7)
        self.b6 = Button(self, text="New Month", width=10)
        self.b6.grid(row=6, column=7)
        self.b7 = Button(self, text="Delete", width=10)
        self.b7.grid(row=7, column=7)
        self.b8 = Button(self, text="Close", width=10, command=self.destroy)
        self.b8.grid(row=8, column=7)

    def open_config(self):
        config_window = Config(self)
        config_window.grab_set()

    def open_addline(self):
        addline_window = AddLineWindow(self)
        addline_window.grab_set()

    def open_modifyline(self):
        modify_window = ModifyLineWindow(self)
        modify_window.grab_set()

    def open_search(self):
        search_window = SearchLineWindow(self)
        search_window.grab_set()

    def refresh(self):
        self.list1.delete(0,END)
        for row in backend.view():
           self.list1.insert(END, row)

    #TODO: implement class, add button, and write description
    #def open_about(self):
    #    about_window = AboutWindow(self)
    #    about_window.grab_set()


class Config(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        #self.geometry('300x100')
        self.title('Configuration')
        self.cl1 = Label(self, text="Current config")
        self.cl1.grid(row=0, column=1)
        self.clb1 = Listbox(self, height=1, width=64)
        self.clb1.grid(row=1, column=1, columnspan=3)
        self.cl2 = Label(self, text="New config")
        self.cl2.grid(row=2, column=1)
        self.ce1_value = StringVar()
        self.ce2_value = StringVar()
        self.ce3_value = IntVar()
        #TODO: add default or labels for entry textboxes
        self.ce1 = Entry(self, textvariable=self.ce1_value)
        self.ce2 = Entry(self, textvariable=self.ce2_value)
        self.ce3 = Entry(self, textvariable=self.ce3_value)
        self.ce1.grid(row=3, column=1)
        self.ce2.grid(row=3, column=2)
        self.ce3.grid(row=3, column=3)
        self.cb1 = Button(self, text="Update config", width=10)
        self.cb1.grid(row=4, column=1)
        self.cb2 = Button(self, text="Close", width=10, command=self.destroy)
        self.cb2.grid(row=4, column=2)


class AddLineWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        #self.geometry('300x100')
        self.title('Add new line')
        self.ae1_value = DoubleVar()
        self.ae2_value = IntVar()
        self.ae3_value = StringVar()
        self.ae1 = Entry(self, textvariable=self.ae1_value)
        self.ae2 = Entry(self, textvariable=self.ae2_value)
        self.ae3 = Entry(self, textvariable=self.ae3_value)
        self.al1 = Label(self, text="Amount")
        self.al2 = Label(self, text="Category")
        self.al3 = Label(self, text="Description")
        self.ae1.grid(row=1, column=1)
        self.ae2.grid(row=1, column=2)
        self.ae3.grid(row=1, column=3)
        self.al1.grid(row=0, column=1)
        self.al2.grid(row=0, column=2)
        self.al3.grid(row=0, column=3)
        self.ab1 = Button(self, text="Search", width=10)
        self.ab1.grid(row=4, column=1)
        self.ab2 = Button(self, text="Close", width=10, command=self.destroy)
        self.ab2.grid(row=4, column=2)


class ModifyLineWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        #self.geometry('300x100')
        self.title('Modify line')
        self.me1_value = DoubleVar()
        self.me2_value = IntVar()
        self.me3_value = StringVar()
        self.me1 = Entry(self, textvariable=self.me1_value)
        self.me2 = Entry(self, textvariable=self.me2_value)
        self.me3 = Entry(self, textvariable=self.me3_value)
        self.ml1 = Label(self, text="Amount")
        self.ml2 = Label(self, text="Category")
        self.ml3 = Label(self, text="Description")
        self.me1.grid(row=1, column=1)
        self.me2.grid(row=1, column=2)
        self.me3.grid(row=1, column=3)
        self.ml1.grid(row=0, column=1)
        self.ml2.grid(row=0, column=2)
        self.ml3.grid(row=0, column=3)
        self.mb1 = Button(self, text="Modify", width=10)
        self.mb1.grid(row=4, column=1)
        self.mb2 = Button(self, text="Close", width=10, command=self.destroy)
        self.mb2.grid(row=4, column=2)


class SearchLineWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        #self.geometry('300x100')
        self.title('Search')
        self.se1_value = DoubleVar()
        self.se2_value = IntVar()
        self.se3_value = StringVar()
        self.se1 = Entry(self, textvariable=self.se1_value)
        self.se2 = Entry(self, textvariable=self.se2_value)
        self.se3 = Entry(self, textvariable=self.se3_value)
        self.sl1 = Label(self, text="Amount")
        self.sl2 = Label(self, text="Category")
        self.sl3 = Label(self, text="Description")
        self.se1.grid(row=1, column=1)
        self.se2.grid(row=1, column=2)
        self.se3.grid(row=1, column=3)
        self.sl1.grid(row=0, column=1)
        self.sl2.grid(row=0, column=2)
        self.sl3.grid(row=0, column=3)
        self.sb1 = Button(self, text="Search", width=10, command=self.search)
        self.sb1.grid(row=4, column=1)
        self.sb2 = Button(self, text="Close", width=10, command=self.destroy)
        self.sb2.grid(row=4, column=2)

    def search(self):
        app.list1.delete(0,END)
        for row in backend.search(self.se1_value.get(), self.se2_value.get(), self.se3_value.get()):
            #TODO: need to search by more than 1 parameter
            # (e.g. category+description does not work) and
            # and fix error messages (missing amount throws error)
            #print(self.se1_value.get())
            #print(self.se2_value.get())
            #print(self.se3_value.get())
            app.list1.insert(END, row)


# TODO: info button for description of software usage
#class AboutWindow(Toplevel):
#    def __init__(self, parent):
#        super().__init__(parent)


if __name__ == "__main__":
    app = App()
    app.mainloop()