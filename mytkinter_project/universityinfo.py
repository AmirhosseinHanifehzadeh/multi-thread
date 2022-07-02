from tkinter import *
import sqlite3

conn = sqlite3.connect('information.db')
c = conn.cursor()

root = Tk()
root.title('St. info')
root.geometry('350x400')

# c.execute(""" CREATE TABLE information (
#   first_name text,
#    last_name text,
#    city text,
#    university_id integer
# )""")



# start functions
def database_add():
    conn = sqlite3.connect('information.db')
    c = conn.cursor()
    # adding to database code
    c.execute('INSERT INTO information VALUES (:f_name, :l_name, :city, :university_id)',
              {
                  'f_name': first_name_input.get(),
                  'l_name': last_name_input.get(),
                  'city': city_input.get(),
                  'university_id': university_id_input.get()
              }
              )

    # clear text boxes
    first_name_input.delete(0, END)
    last_name_input.delete(0, END)
    city_input.delete(0, END)
    university_id_input.delete(0, END)

    conn.commit()

    conn.close()


def show():
    conn = sqlite3.connect('information.db')
    c = conn.cursor()

    c.execute('SELECT *,oid FROM information')
    records = c.fetchall()
    print_records = ''
    for record in records:
        print_records += str(record) + '\n'
    records_label = Label(root, text=print_records)
    records_label.grid(row=8, column=0, columnspan=2)

    conn.commit()

    conn.close()


def delete():
    conn = sqlite3.connect('information.db')
    c = conn.cursor()
    




    conn.commit()

    conn.close()

# start create LABELS
first_name_label = Label(root, text='first name : ')
first_name_label.grid(row=1, column=0, padx=5, pady=5)
last_name_label = Label(root, text='last name :')
last_name_label.grid(row=2, column=0)
city_label = Label(root, text='city :')
city_label.grid(row=3, column=0)
university_id_label = Label(root, text='id :')
university_id_label.grid(row=4, column=0)
# finish LABELS

# start create inputs
first_name_input = Entry(root, width=40, bd=3)
first_name_input.grid(row=1, column=1)
last_name_input = Entry(root, width=40, bd=3)
last_name_input.grid(row=2, column=1)
city_input = Entry(root, width=40, bd=3)
city_input.grid(row=3, column=1)
university_id_input = Entry(root, width=40, bd=3)
university_id_input.grid(row=4, column=1)
# finish inputs

# start create buttons
database_add_btn = Button(root, text='Add to database',
                          bg='green', fg='white', width=44, command=database_add)
database_add_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=5)
show_database_btn = Button(root, text='Show Database',
                           bg='black', fg='white', width=44, command=show)
show_database_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=5)
delete_btn = Button(root, text='Delete', bg='red', fg='white', width=44, command=delete)
delete_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=5)
# finish create buttons


conn.commit()

conn.close()

root.mainloop()
