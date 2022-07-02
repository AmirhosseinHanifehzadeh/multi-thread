from tkinter import * 
root = Tk()

def myClick():
    mylabel = Label(root, text='Look! i clicked button.')
    mylabel.pack()

myButton = Button(root, text='Click me',padx=50, pady=50, command=myClick, fg='blue', bg='#787878')
myButton.pack()


root.mainloop()
