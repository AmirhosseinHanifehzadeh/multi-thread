from tkinter import * 
from PIL import ImageTk, Image


root = Tk()
root.title('images')

""" my_img = ImageTk.PhotoImage(Image.open("eifel.jpeg"))
my_label = Label(image=my_img)
my_label.pack() """





btn_quit = Button(root, text='quit', command=root.quit)
btn_quit.pack()
root.mainloop()