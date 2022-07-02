from tkinter import *

root = Tk()
root.geometry('400x400')

def slider():
    my_label = Label(root, text=horizotal.get())
    my_label.pack()
    root.geometry(str(horizotal.get()) + 'x400')

vertical = Scale(root, from_=0, to=200)
vertical.pack()

horizotal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizotal.pack()

my_label = Label(root, text=horizotal.get()).pack()
my_btn = Button(root, text='Click', command=slider).pack()





root.mainloop()