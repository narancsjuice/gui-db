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

        self.l2 = Label(self, text="Spending", width=15)
        self.l2.grid(row=0, column=2)
        self.t2 = Text(self, height=1, width=15)
        self.t2.grid(row=0, column=3)

        self.l3 = Label(self, text="Left-over", width=15)
        self.l3.grid(row=0, column=4)
        self.t3 = Text(self, height=1, width=15)
        self.t3.grid(row=0, column=5)

        self.l4 = Label(self, text="Savings", width=15)
        self.l4.grid(row=0, column=6)
        self.t4 = Text(self, height=1, width=15)
        self.t4.grid(row=0, column=7)

        #TODO: refresh this, maybe move all to function along with state=disabled
        # also add symbols to lines (?)
        self.set_value(self.t1, str(backend.sum_income()[0][0]) + " " + self.get_symbol())
        self.set_value(self.t2, str(backend.sum_spendings()[0][0]) + " " + self.get_symbol())
        self.set_value(self.t3, str(float(backend.sum_income()[0][0] - backend.sum_spendings()[0][0])) + " " + self.get_symbol())
        self.set_value(self.t4, str(backend.sum_savings()[0][0]) + " " + self.get_symbol())

        self.t1.configure(state="disabled")
        self.t2.configure(state="disabled")
        self.t3.configure(state="disabled")
        self.t4.configure(state="disabled")

        # TODO: better listbox with columns

        # listbox and scrollbar
        self.list1 = Listbox(self, height=40, width=120, exportselection=False)
        self.list1.grid(row=1, column=0, rowspan=48, columnspan=6)

        # load list items
        for row in backend.view_lines():
            self.list1.insert(END, row)

        self.scroll1 = Scrollbar(self)
        self.scroll1.grid(row=1, column=6, rowspan=48)

        self.list1.configure(yscrollcommand=self.scroll1.set)
        self.scroll1.configure(command=self.list1.yview)
        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

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
        #TODO: new period function
        self.b6 = Button(self, text="New Month", width=10)
        self.b6.grid(row=6, column=7)
        self.b7 = Button(self, text="Delete", width=10, command=self.delete)
        self.b7.grid(row=7, column=7)
        self.b8 = Button(self, text="Close", width=10, command=self.destroy)
        self.b8.grid(row=8, column=7)

    def get_selected_row(self, event):
        try:
            global selected_tuple
            index = self.list1.curselection()[0]
            selected_tuple = self.list1.get(index)
        except IndexError:
            pass

    def open_config(self):
        config_window = Config(self)
        config_window.grab_set()

    def open_addline(self):
        addline_window = AddLineWindow(self)
        addline_window.grab_set()

    def open_modifyline(self):
        #TODO: modify window should not open if no row is selected
        # or should not show values already deleted (delete value -> open shows
        # already deleted values on modify window)
        modify_window = ModifyLineWindow(self)
        modify_window.grab_set()

    def open_search(self):
        search_window = SearchLineWindow(self)
        search_window.grab_set()

    def delete(self):
        try:
            backend.delete_line(selected_tuple[0])
            self.refresh()
        except NameError:
            pass

    def get_symbol(self):
        symbol = backend.view_config()[0][2]
        return symbol

    def refresh(self):
        self.list1.delete(0,END)
        for row in backend.view_lines():
           self.list1.insert(END, row)

    #TODO: set_value does not refresh values, change this later, maybe add new
    # table to store the values and similarly to refresh just requery
    def set_value(self, textbox, value):
        try:
            textbox.delete(1.0, END)
            textbox.insert(END, value)
        except TclError:
            textbox.insert(END, 0)

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
        self.cl1.grid(row=0, column=1)
        self.clb1 = Listbox(self, height=1, width=64)
        self.clb1.grid(row=1, column=1, columnspan=3)
        self.cl2 = Label(self, text="New config")
        self.cl2.grid(row=2, column=1)
        self.ce1_value = StringVar()
        self.ce2_value = StringVar()
        self.ce3_value = IntVar()
        self.ce1 = Entry(self, textvariable=self.ce1_value)
        self.ce2 = Entry(self, textvariable=self.ce2_value)
        self.ce3 = Entry(self, textvariable=self.ce3_value)
        self.show_value(self.ce1, backend.view_config()[0][1])
        self.show_value(self.ce2, backend.view_config()[0][2])
        self.show_value(self.ce3, backend.view_config()[0][3])
        self.ce1.grid(row=3, column=1)
        self.ce2.grid(row=3, column=2)
        self.ce3.grid(row=3, column=3)

        self.cb1 = Button(self, text="Update config", width=10, command=self.update_config)
        self.cb1.grid(row=4, column=1)
        self.cb2 = Button(self, text="Close", width=10, command=self.destroy)
        self.cb2.grid(row=4, column=2)

        for row in backend.view_config():
            self.clb1.insert(END, row)

    def update_config(self):
        backend.modify_config(self.ce1_value.get(), self.ce2_value.get(), self.ce3_value.get())
        self.clb1.delete(0,END)
        for row in backend.view_config():
            self.clb1.insert(END, row)

    def show_value(self, entry, value):
        entry.delete(0, END)
        entry.insert(END, value)

class AddLineWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        #self.geometry('300x100')
        self.title('Add new line')
        self.ae1_value = DoubleVar()
        self.ae2_value = IntVar()
        self.ae3_value = StringVar()
        self.ae1 = Entry(self, textvariable=self.ae1_value)
        #self.ae2 = Entry(self, textvariable=self.ae2_value)
        self.ae3 = Entry(self, textvariable=self.ae3_value)
        self.al1 = Label(self, text="Amount")
        self.al2 = Label(self, text="Category")
        self.al3 = Label(self, text="Description")
        self.ae1.grid(row=1, column=1)
        #self.ae2.grid(row=1, column=2)
        self.ae3.grid(row=1, column=3)
        self.al1.grid(row=0, column=1)
        self.al2.grid(row=0, column=2)
        self.al3.grid(row=0, column=3)
        self.ab1 = Button(self, text="Add", width=10, command=self.add)
        self.ab1.grid(row=4, column=1)
        self.ab2 = Button(self, text="Close", width=10, command=self.destroy)
        self.ab2.grid(row=4, column=2)

        dd_list = list(backend.view_categories())
        self.dd1_value = StringVar(self)
        self.dd1_value.set(dd_list[0])
        self.dd1 = OptionMenu(self, self.dd1_value, *dd_list)
        self.dd1.config(width=15, height=1)
        self.dd1.grid(row=1, column=2)

    def add(self):
        category = self.dd1_value.get()[2:-3]
        category_id = backend.get_categoryid(category)[0][0]
        backend.add_line(self.ae1_value.get(), category_id, self.ae3_value.get())
        app.refresh()


class ModifyLineWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        #self.geometry('300x100')
        self.title('Modify line')
        self.me1_value = DoubleVar()
        self.me2_value = IntVar()
        self.me3_value = StringVar()
        self.me1 = Entry(self, textvariable=self.me1_value)
        #self.me2 = Entry(self, textvariable=self.me2_value)
        self.me3 = Entry(self, textvariable=self.me3_value)
        self.show_value(self.me1, selected_tuple[1])
        #self.show_value(self.me2, selected_tuple[2])
        self.show_value(self.me3, selected_tuple[3])
        self.ml1 = Label(self, text="Amount")
        self.ml2 = Label(self, text="Category")
        self.ml3 = Label(self, text="Description")
        self.me1.grid(row=1, column=1)
        #self.me2.grid(row=1, column=2)
        self.me3.grid(row=1, column=3)
        self.ml1.grid(row=0, column=1)
        self.ml2.grid(row=0, column=2)
        self.ml3.grid(row=0, column=3)
        self.mb1 = Button(self, text="Modify", width=10, command=self.modify)
        self.mb1.grid(row=4, column=1)
        self.mb2 = Button(self, text="Close", width=10, command=self.destroy)
        self.mb2.grid(row=4, column=2)

        self.dd1_value = StringVar(self)
        self.dd1_value.set(selected_tuple[2])
        self.dd1 = OptionMenu(self, self.dd1_value, *self.create_dropdown())
        self.dd1.config(width=15, height=1)
        self.dd1.grid(row=1, column=2)

    #TODO: either: require all fields, or define default to be null so only fields
    # get modified that are changed by user (amount and category are 0 right now and modify values)
    def modify(self):
        category = self.dd1_value.get()
        category_id = backend.get_categoryid(category)[0][0]
        backend.modify_line(selected_tuple[0], self.me1_value.get(), category_id, self.me3_value.get())
        app.refresh()

    def create_dropdown(self):
        dropdown_list = []
        categories_list = backend.view_categories()
        for category in categories_list:
            category = category[0]
            dropdown_list.append(category)
        return dropdown_list

    def show_value(self, entry, value):
        entry.delete(0, END)
        entry.insert(END, value)


class SearchLineWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        #self.geometry('300x100')
        self.title('Search')
        self.se1_value = DoubleVar()
        self.se2_value = IntVar()
        self.se3_value = StringVar()
        self.se1 = Entry(self, textvariable=self.se1_value)
        #self.se2 = Entry(self, textvariable=self.se2_value)
        self.se3 = Entry(self, textvariable=self.se3_value)
        self.sl1 = Label(self, text="Amount")
        self.sl2 = Label(self, text="Category")
        self.sl3 = Label(self, text="Description")
        self.se1.grid(row=1, column=1)
        #self.se2.grid(row=1, column=2)
        self.se3.grid(row=1, column=3)
        self.sl1.grid(row=0, column=1)
        self.sl2.grid(row=0, column=2)
        self.sl3.grid(row=0, column=3)
        self.sb1 = Button(self, text="Search", width=10, command=self.search)
        self.sb1.grid(row=4, column=1)
        self.sb2 = Button(self, text="Close", width=10, command=self.destroy)
        self.sb2.grid(row=4, column=2)
        self.dd1_value = IntVar(self)

        self.dd1_value.set("default")
        self.dd1 = OptionMenu(self, self.dd1_value, "1", "2", "3")
        self.dd1.config(width=15, height=1)
        self.dd1.grid(row=1, column=2)

    def search(self):
        app.list1.delete(0,END)
        for row in backend.search_line(self.se1_value.get(), self.se2_value.get(), self.se3_value.get()):
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