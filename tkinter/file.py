from tkinter import * 
from tkinter import filedialog
from PIL import Image, ImageTk

root = Tk()

def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir='/document/coding train/python training', filetypes=(('png files', '*.png'), ('all files', '*.*')))
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image)
    my_image_label.pack()

my_btn = Button(root, text='Open file', command=open)
my_btn.pack()
root.mainloop()