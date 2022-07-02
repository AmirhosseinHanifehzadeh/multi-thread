'''
this program has these options:
1. restart: this option makes a new round (without reset of counters of wins )
2. total restart: this option make a new set ( it reset counter of palyer 1 wins and player2 wins )
3. it shows how much time you play 
4. it shows which player is turn 
'''

from tkinter import *
from tkinter import messagebox


root = Tk()
root.title('Tic Tac Toe')

counter = 0
click = True
player1NumWin = 0
player2NumWin = 0

def reset():
    global winner , counter
    buttons()
    winner = False
    counter = 0


def disable_btn():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

def totalRestart():
    global player1NumWin , player2NumWin , winner, counter
    buttons()
    player2NumWin = 0
    player1NumWin = 0
    winner = False
    counter = 0


def updateShowTimer():
    ''' function to update the timer  '''
    minute = 0
    second = 0
    def inner():
        nonlocal second, minute
        if second == 59:
            second = 0
            minute += 1
        second += 1
        timer.config(text=f'{minute} : {second}')
        timer.after(1000, inner)
    return inner

updateTimer = updateShowTimer()

def win():
    global player1NumWin , player2NumWin
    global winner
    winner = False

    if b1['text'] == b2['text'] == b3['text'] != '':
        b1.config(bg='green')
        b2.config(bg='green')
        b3.config(bg='green')
        if b1['text'] == 'X':
            player1NumWin += 1
        else:
            player2NumWin += 1
        messagebox.showinfo('congratulations', f"{b1['text']} palyer wins. \n player 1 wins : {player1NumWin} \n player 2 wins : {player2NumWin}")
        winner = True
            
    elif b4['text'] == b5['text'] == b6['text'] != '':
        b4.config(bg='green')
        b5.config(bg='green')
        b6.config(bg='green')

        if b4['text'] == 'X':
            player1NumWin += 1
        else:
            player2NumWin += 1
        messagebox.showinfo('congratulations', f"{b4['text']} palyer wins.\n player 1 wins : {player1NumWin} \n player 2 wins : {player2NumWin}")
        winner = True
    elif b7['text'] == b8['text'] == b9['text'] != '':
        b7.config(bg='green')
        b8.config(bg='green')
        b8.config(bg='green')

        if b7['text'] == 'X':
            player1NumWin += 1
        else:
            player2NumWin += 1
        messagebox.showinfo('congratulations', f"{b7['text']} palyer wins.\n player 1 wins : {player1NumWin} \n player 2 wins : {player2NumWin}")
        winner = True

    elif b1['text'] == b4['text'] == b7['text'] != '':
        b1.config(bg='green')
        b4.config(bg='green')
        b7.config(bg='green')

        if b1['text'] == 'X':
            player1NumWin += 1
        else:
            player2NumWin += 1
        messagebox.showinfo('congratulations', f"{b1['text']} palyer wins.\n player 1 wins : {player1NumWin} \n player 2 wins : {player2NumWin}")
        winner = True

    elif b2['text'] == b5['text'] == b8['text'] != '':
        b5.config(bg='green')
        b2.config(bg='green')
        b8.config(bg='green')

        if b2['text'] == 'X':
            player1NumWin += 1
        else:
            player2NumWin += 1
        messagebox.showinfo('congratulations', f"{b2['text']} palyer wins.\n player 1 wins : {player1NumWin} \n player 2 wins : {player2NumWin}")
        winner = True

    elif b9['text'] == b6['text'] == b3['text'] != '':
        b9.config(bg='green')
        b6.config(bg='green')
        b3.config(bg='green')

        if b3['text'] == 'X':
            player1NumWin += 1
        else:
            player2NumWin += 1
        messagebox.showinfo('congratulations', f"{b3['text']} palyer wins.\n player 1 wins : {player1NumWin} \n player 2 wins : {player2NumWin}")
        winner = True

    elif b1['text'] == b5['text'] == b9['text'] != '':
        b1.config(bg='green')
        b5.config(bg='green')
        b9.config(bg='green')

        if b1['text'] == 'X':
            player1NumWin += 1
        else:
            player2NumWin += 1
        messagebox.showinfo('congratulations', f"{b1['text']} palyer wins.\n player 1 wins : {player1NumWin} \n player 2 wins : {player2NumWin}")
        winner = True

    elif b7['text'] == b5['text'] == b3['text'] != '':
        b7.config(bg='green')
        b5.config(bg='green')
        b3.config(bg='green')

        if b3['text'] == 'X':
            player1NumWin += 1
        else:
            player2NumWin += 1
        messagebox.showinfo('congratulations', f"{b3['text']} palyer wins.\n player 1 wins : {player1NumWin} \n player 2 wins : {player2NumWin}")
        winner = True

    if winner == True:
        disable_btn()

    if counter == 9 and winner != True:
        disable_btn()
        messagebox.showinfo('equal', f"player 1 wins : {player1NumWin} \n player 2 wins : {player2NumWin}")


def btnClick(btn):
    global counter
    global click
    global playerturn

    if btn['text'] == '' and click:
        counter += 1
        click = False
        btn['text'] = 'X'
        win()
        playerturn['text'] = 'Turn : O'

    elif btn['text'] == '' and click == False:
        counter += 1
        click = True
        btn['text'] = 'O'
        win()
        playerturn['text'] = 'Turn : X'



# labels
def buttons():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9, timer, updateTimer
    b1 = Button(root, text="", font=('helvetica', 20), height=3,
                width=6, bg='silver', command=lambda: btnClick(b1))
    b2 = Button(root, text="", font=('helvetica', 20), height=3,
                width=6, bg='silver', command=lambda: btnClick(b2))
    b3 = Button(root, text="", font=('helvetica', 20), height=3,
                width=6, bg='silver', command=lambda: btnClick(b3))
    b4 = Button(root, text="", font=('helvetica', 20), height=3,
                width=6, bg='silver', command=lambda: btnClick(b4))
    b5 = Button(root, text="", font=('helvetica', 20), height=3,
                width=6, bg='silver', command=lambda: btnClick(b5))
    b6 = Button(root, text="", font=('helvetica', 20), height=3,
                width=6, bg='silver', command=lambda: btnClick(b6))
    b7 = Button(root, text="", font=('helvetica', 20), height=3,
                width=6, bg='silver', command=lambda: btnClick(b7))
    b8 = Button(root, text="", font=('helvetica', 20), height=3,
                width=6, bg='silver', command=lambda: btnClick(b8))
    b9 = Button(root, text="", font=('helvetica', 20), height=3,
                width=6, bg='silver', command=lambda: btnClick(b9))



    # show on screen
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)
    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)
    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

timer = Label(root, text="0 : 00" ,font=('helvetica' ,20), fg='red' , anchor=CENTER)
updateTimer()
timer.grid(row=3, column=1)

playerturn = Label(root, text='Turn : X',font=('helvetica' ,12), fg='blue',relief=RIDGE)
playerturn.grid(row=3, column=0 , ipadx=10 , sticky=W)

myMenu = Menu(root)
root.config(menu=myMenu)
optionMenu = Menu(myMenu, tearoff=False)
myMenu.add_cascade(label="option", menu=optionMenu)
optionMenu.add_command(label='reset' , command=reset)
optionMenu.add_command(label='total start' , command=totalRestart)

reset()

root.mainloop()
