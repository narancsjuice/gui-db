import sqlite3


def connect():
    con = sqlite3.connect("personal_finance.db")
    cur = con.cursor()

    # config table
    cur.execute("CREATE TABLE IF NOT EXISTS"
                " config "
                "(id INTEGER PRIMARY KEY,"
                " currency TEXT,"
                " symbol TEXT,"
                " income INTEGER)")

    #TODO: insert default into config

    # spendings categories table
    cur.execute("CREATE TABLE IF NOT EXISTS"
                " categories "
                "(id INTEGER PRIMARY KEY,"
                " category TEXT)")

    # spendings/savings table
    cur.execute("CREATE TABLE IF NOT EXISTS"
                " account "
                "(id INTEGER PRIMARY KEY,"
                " amount DECIMAL(10,2),"
                " category_id INTEGER,"
                " description TEXT,"
                " FOREIGN KEY(category_id) REFERENCES categories(id))")
    con.commit()
    con.close()


def add_line(amount, category_id, description):
    con = sqlite3.connect("personal_finance.db")
    cur = con.cursor()
    cur.execute("INSERT INTO account VALUES (NULL,?,?,?)", (amount, category_id, description))
    con.commit()
    con.close()


def view():
    con = sqlite3.connect("personal_finance.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM account")
    rows = cur.fetchall()
    con.close()
    return rows


def search(amount="", category_id="", description=""):
    con = sqlite3.connect("personal_finance.db")
    cur = con.cursor()
    #TODO: more intelligent description search (find substrings)?
    cur.execute("SELECT * FROM account WHERE amount=? OR category_id=? OR description=?", (amount, category_id, description))
    rows = cur.fetchall()
    con.close()
    return rows


def delete_line(id):
    con = sqlite3.connect("personal_finance.db")
    cur = con.cursor()
    cur.execute("DELETE FROM account WHERE id=?", (id,))
    con.commit()
    con.close()


def modify_line(id, amount, category_id, description):
    con = sqlite3.connect("personal_finance.db")
    cur = con.cursor()
    cur.execute("UPDATE account SET amount=?, category_id=?, description=? WHERE id=?", (amount, category_id, description, id))
    con.commit()
    con.close()

#TODO: update config button backend code (update row)
#TODO: add/remove/update categories backend code
#TODO: date for lines

#def close():
    #main_window.destroy()

connect()