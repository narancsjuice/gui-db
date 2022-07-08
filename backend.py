import sqlite3

#TODO: new function that send leftover to savings, resets income
#TODO: every spending, saving, money calculation should show the symbol

def connect():
    con = sqlite3.connect("personal_finance.db")
    cur = con.cursor()

    #TODO: income to decimal, savings as decimal
    #TODO: income is nullable, in later calculation this should be handled if the user has no income

    # config table
    cur.execute("CREATE TABLE IF NOT EXISTS"
                " config "
                "(id INTEGER PRIMARY KEY,"
                " currency TEXT NOT NULL,"
                " symbol TEXT NOT NULL,"
                " income INTEGER)")

    # inserting default value
    cur.execute("INSERT INTO config(id, currency, symbol, income)"
                " SELECT 1, 'Hungarian Forint', 'HUF', 350000"
                " WHERE NOT EXISTS (SELECT * FROM config WHERE id = 1)")

    #TODO: insert default into config or create table with default values

    # spendings categories table
    cur.execute("CREATE TABLE IF NOT EXISTS"
                " categories "
                "(id INTEGER PRIMARY KEY,"
                " category TEXT,"
                " type INTEGER)")

    #TODO: use dates for lines

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


def view_lines():
    con = sqlite3.connect("personal_finance.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM account")
    rows = cur.fetchall()
    con.close()
    return rows


def view_config():
    con = sqlite3.connect("personal_finance.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM config")
    rows = cur.fetchall()
    con.close()
    return rows


def search_line(amount="", category_id="", description=""):
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


def modify_config(currency, symbol, income):
    con = sqlite3.connect("personal_finance.db")
    cur = con.cursor()
    cur.execute("UPDATE config SET currency=?, symbol=?, income=? WHERE id=1", (currency, symbol, income))
    con.commit()
    con.close()

#TODO: add/remove/update categories backend code


connect()