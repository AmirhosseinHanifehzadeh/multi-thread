from tkinter import * 
from PIL import Image, ImageTk

root = Tk()
root.title('frames')

frame = LabelFrame(root, text='this is frame ...', padx=5, pady=3)

frame.pack(padx=10, pady=10)

b = Button(frame, text='click')

b.pack()


root.mainloop()