from tkinter import *
from types import BuiltinFunctionType
root = Tk()
root.title('claculator')

e = Entry(root, width=50, borderwidth=3)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def btn_add():
    pass


btn_1 = Button(root, text='1', pady=20, padx=40, command=btn_add)
btn_2 = Button(root, text='2', pady=20, padx=40, command=btn_add)
btn_3 = Button(root, text='3', pady=20, padx=40, command=btn_add)
btn_4 = Button(root, text='4', pady=20, padx=40, command=btn_add)
btn_5 = Button(root, text='5', pady=20, padx=40, command=btn_add)
btn_6 = Button(root, text='6', pady=20, padx=40, command=btn_add)
btn_7 = Button(root, text='7', pady=20, padx=40, command=btn_add)
btn_8 = Button(root, text='8', pady=20, padx=40, command=btn_add)
btn_9 = Button(root, text='9', pady=20, padx=40, command=btn_add)
btn_0 = Button(root, text='0', pady=20, padx=40, command=btn_add)
btn_equal = Button(root, Text='=', padx=91, pady=20, command=btn_add)
btn_clear = Button(root, Text='clear', padx=79, pady=20, command=btn_add)
btn_plus = Button(root, Text='+', padx=39, pady=20, command=btn_add)
# pyt buttons on the screen
btn_1.grid(row=3, column=0)
btn_2.grid(row=3, column=1)
btn_3.grid(row=3, column=2)

btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)

btn_7.grid(row=1, column=0)
btn_8.grid(row=1, column=1)
btn_9.grid(row=1, column=2)

btn_0.grid(row=4, column=0)

btn_clear.grid(row=4, column=0)
btn_equal.grid()
btn_plus.grid(row=5, column=0)

root.mainloop()