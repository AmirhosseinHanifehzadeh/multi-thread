from tkinter import * 
from PIL import Image, ImageTk
root = Tk()
root.title('new window')

top = Toplevel()

lbl = Label(top, text='hello world 2').pack()
lbl1 = Label(root, text='hello world 1').pack()




mainloop()