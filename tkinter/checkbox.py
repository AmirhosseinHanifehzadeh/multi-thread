from tkinter import * 

root = Tk()

def show():
    my_label = Label(root, text=var.get())
    my_label.pack()

var = StringVar()

c = Checkbutton(root, text='check 1', variable=var, onvalue='on', offvalue='off')
c.deselect()
c.pack()

my_btn = Button(root, text='show', command= show)
my_btn.pack()


root.mainloop()