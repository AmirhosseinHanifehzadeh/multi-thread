from tkinter import * 

root = Tk()

r = IntVar()
r.set('2')

def clicked(value):
    mylabel = Label(root, text=value)
    mylabel.pack()  


Radiobutton(root, text='Option 1', variable=r, value=1, command=lambda: clicked(r.get())).pack()
Radiobutton(root, text='Option 2', variable=r, value=2, command=lambda: clicked(r.get())).pack()

mylabel = Label(root, text=r.get()).pack()


root.mainloop()