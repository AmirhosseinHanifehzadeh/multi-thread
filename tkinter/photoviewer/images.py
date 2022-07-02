from os import terminal_size
from tkinter import * 
from PIL import Image, ImageTk

root = Tk()
root.title('image viewer')

def forward(image_number):
    global my_label
    global btn_forward
    global btn_back

    my_label.grid_forget()
    
    my_label = Label(image= image_list[image_number -1])
    btn_forward = Button(root, text='>>', command=lambda: forward(image_number + 1))
    btn_back = Button(root, text='<<', command=lambda: back(image_number - 1))

    if image_number == 3:
        btn_forward = Button(root, text='>>', state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    btn_back.grid(row=1, column=0)
    btn_forward.grid(row=1, column=2)

    status = Label(root, text='Image' + str(image_number) +'of' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)




def back(image_number):
    global my_label
    global btn_forward
    global btn_back

    my_label.grid_forget()
    
    my_label = Label(image= image_list[image_number -1])
    btn_forward = Button(root, text='>>', command=lambda: forward(image_number + 1))
    btn_back = Button(root, text='<<', command=lambda: back(image_number - 1))

    if image_number == 1:
        btn_back = Button(root, text='<<', state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    btn_back.grid(row=1, column=0)
    btn_forward.grid(row=1, column=2)

    status = Label(root, text='Image' + str(image_number) +'of' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

my_img1 = ImageTk.PhotoImage(Image.open('benz.jpeg'))
my_img2 = ImageTk.PhotoImage(Image.open('bmw.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open('romeo.jpg'))


image_list = [my_img1, my_img2, my_img3]

status = Label(root, text='Image 1 of ' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

btn_back = Button(root, text='<<', command=back)
btn_exit = Button(root, text='Exit', command=root.quit)
btn_forward = Button(root, text='>>', command=lambda:forward(2))

btn_back.grid(row=1, column=0)
btn_forward.grid(row=1, column=2)
btn_exit.grid(row=1, column=1)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)



root.mainloop()
