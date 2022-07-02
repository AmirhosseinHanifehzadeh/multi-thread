from tkinter import *
from tkinter import messagebox

root = Tk()

def popup():
    messagebox.showinfo('this is my popup', 'hello')

Button(root, text='popup', command=popup).pack()

root.mainloop()

#showinfo, showwarning, showeror, askquestion, askokcancel, askyesno