from tkinter import *
def click(r, c):
    if not btns[r][c]['text'] and not win[0]:
        btns[r][c]['text'] = players[turn[0]]
        btns[r][c]['fg'] = colors[turn[0]]
        if any(all(btns[i][j]['text'] == players[turn[0]] for i, j in line) for line in wins):
            win[0] = True
            label.config(text=f"{players[turn[0]]} wins!")
        else:
            turn[0] ^= 1
            label.config(text=f"{players[turn[0]]}'s turn")

def reset():
    for r in range(3):
        for c in range(3):
            btns[r][c].config(text='', fg='black')
    turn[0], win[0] = 0, False
    label.config(text="X's turn")

root = Tk()
root.title("Tic Tac Toe")
players, colors = ['X', 'O'], ['deepskyblue', 'olivedrab1']
turn, win = [0], [False]

btns = [[Button(root, text='', font='Arial 20', width=10, height=5, bg='black',
                command=lambda r=r, c=c: click(r, c)) for c in range(3)] for r in range(3)]
for r in range(3): [btns[r][c].grid(row=r, column=c) for c in range(3)]

wins = [[(i, j) for j in range(3)] for i in range(3)] + \
       [[(i, j) for i in range(3)] for j in range(3)] + \
       [[(i, i) for i in range(3)], [(i, 2 - i) for i in range(3)]]

label = Label(root, text="X's turn", font='Arial 15', bg='lightgreen')
label.grid(row=3, column=0, columnspan=3, sticky='we')
Button(root, text='Reset', font='Arial 12', bg='lightblue', command=reset).grid(row=4, column=0, columnspan=3, sticky='we')
root.mainloop()
