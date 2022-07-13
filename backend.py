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
                " income DECIMAL(10,2))")

    # inserting default value
    cur.execute("INSERT INTO config (id, currency, symbol, income)"
                " SELECT 1, 'Hungarian Forint', 'HUF', 350000"
                " WHERE NOT EXISTS (SELECT * FROM config WHERE id = 1)")

    # spendings categories table
    cur.execute("CREATE TABLE IF NOT EXISTS"
                " categories "
                "(id INTEGER PRIMARY KEY,"
                " category TEXT,"
                " type INTEGER)")

    # list of categories to insert into categories table
    categories_list = [(1, "Salary", 1),
                       (2, "Bonus", 1),
                       (3, "Gift", 1),
                       (4, "Government Assistance", 1),
                       (5, "Housing", 2),
                       (6, "Groceries", 2),
                       (7, "Utilities", 2),
                       (8, "Transportation", 2),
                       (9, "Healthcare", 2),
                       (10, "Insurance", 2),
                       (11, "Household items", 2),
                       (12, "Clothing", 2),
                       (13, "Personal", 2),
                       (14, "Entertainment", 2),
                       (15, "Education", 2),
                       (16, "Gift", 2),
                       (17, "Debt", 2),
                       (18, "Retirement", 2),
                       (19, "Emergency funds", 3),
                       (20, "Long-term savings", 3),
                       (21, "Fun savings", 3)]

    for category in categories_list:
        cur.execute("INSERT INTO categories (id, category, type)"
                    " SELECT ?, ?, ?"
                    " WHERE NOT EXISTS (SELECT * FROM categories WHERE id = ?)", (category[0], category[1], category[2], category[0]))

    #TODO: use dates for lines

    # spendings/savings table
    cur.execute("CREATE TABLE IF NOT EXISTS"
                " account "
                "(id INTEGER PRIMARY KEY,"
                " amount DECIMAL(10,2) NOT NULL,"
                " category_id INTEGER NOT NULL,"
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
    cur.execute("SELECT id, amount, (SELECT category FROM categories WHERE categories.id=category_id), description FROM account")
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


def view_categories():
    con = sqlite3.connect("personal_finance.db")
    cur = con.cursor()
    cur.execute("SELECT category FROM categories")
    rows = cur.fetchall()
    con.close()
    return rows


def get_categoryid(category):
    con = sqlite3.connect("personal_finance.db")
    cur = con.cursor()
    cur.execute("SELECT id FROM categories WHERE category=?", (category,))
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


def sum_income():
    con = sqlite3.connect("personal_finance.db")
    cur = con.cursor()
    cur.execute("SELECT sum(amount) FROM account LEFT JOIN categories ON category_id=categories.id WHERE type=1")
    rows = cur.fetchall()
    con.close()
    return rows


def sum_spendings():
    con = sqlite3.connect("personal_finance.db")
    cur = con.cursor()
    cur.execute("SELECT sum(amount) FROM account LEFT JOIN categories ON category_id=categories.id WHERE type=2")
    rows = cur.fetchall()
    con.close()
    return rows


def sum_savings():
    con = sqlite3.connect("personal_finance.db")
    cur = con.cursor()
    cur.execute("SELECT sum(amount) FROM account LEFT JOIN categories ON category_id=categories.id WHERE type=3")
    rows = cur.fetchall()
    con.close()
    return rows


connect()