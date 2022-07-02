from tkinter import * 

root = Tk()
root.geometry('400x400')

def show():
    my_label = Label(root, text=clicked.get())
    my_label.pack()

options = ['Monday', 'Tuesday', 'Wendsday', 'Friday']

clicked = StringVar()
clicked.set('Monday')
drop = OptionMenu(root, clicked, 'Monday', 'Tuesday', 'Wendsday', 'Friday')
drop.pack()

var = StringVar()
var.set(options[1])
drop2 = OptionMenu(root, var, options)
drop2.pack()

my_btn = Button(root, text='show selection', command=show).pack()

root.mainloop()