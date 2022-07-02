from tkinter import * 
root = Tk()


txt = StringVar()
e = Entry(root, width=50, bg='#fff', borderwidth=5, textvariable=txt)
e.pack()
e.focus()

def Click():
    hello = 'hello' + e.get()
    mylabel = Label(root, text=hello)
    mylabel.pack()


myButton = Button(root, text='Click', padx=10, command=Click)
myButton.pack()



root.mainloop()