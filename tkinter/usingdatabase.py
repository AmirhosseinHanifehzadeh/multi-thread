from tkinter import *
import sqlite3


root = Tk()
root.title('using database')

conn = sqlite3.connect('address_book.db')
c = conn.cursor()
''''
c.execute("""CREATE TABLE addresses (
    first_name text, 
    last_name text,
    address text, 
    city text, 
    state text,
    zipcode integer
)
""")
'''
f_name = Entry(root, width=30)
f_name.grid(row=0, column=0, padx=20)

l_name = Entry(root, width=30)
l_name.grid(row=0, column=0, padx=20)

address = Entry(root, width=30)
f_name.grid(row=0, column=0, padx=20)

city = Entry(root, width=30)
f_name.grid(row=0, column=0, padx=20)

state = Entry(root, width=30)
f_name.grid(row=0, column=0, padx=20)

zipcode = Entry(root, width=30)
f_name.grid(row=0, column=0, padx=20)





conn.commit()
conn.close()

root.mainloop()