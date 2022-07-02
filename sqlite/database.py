import sqlite3
conn = sqlite3.connect('customer.db')

# create cursor
c = conn.cursor()


c.execute("INSERT INTO customers values ('Setayesh', 'Hanifeh', 'Setayeshe@hanifeh.com')")
c.execute("DELETE from customers WHERE rowid = 6")
c.execute("SELECT rowid,* from customers")
items = c.fetchall()
print(items)

# close our connection
conn.close()
