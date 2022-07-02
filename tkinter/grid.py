from tkinter import * 

root = Tk()

mylabel1 = Label(root, text='helllo').grid(row=0, column=0)
mylabel2 = Label(root, text='my name is amirhossein').grid(row=1, column=5)
mylabel3 = Label(root, text=' ').grid(row=1, column=1)


""" mylabel1.grid(row=0, column=0)
mylabel2.grid(row=1, column=5)
mylabel3.grid(row=1, column=1) """


root.mainloop()