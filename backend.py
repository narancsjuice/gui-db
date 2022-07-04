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

connect()