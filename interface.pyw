# -*- coding: utf-8; -*-
from Tkinter import *
from bs import *

class Btns(object):
    def  __init__(self,size,fr):
        self.btns = []
        for i in xrange(0,size):
            self.btns.append([])
            for j in xrange(0,size):
                btn = Button(fr, width = 4, height= 2, text = ' ')
                btn.grid(row = i, column = j)
                btn.config(state = 'disabled', relief=SUNKEN, borderwidth=1, font = '30')
                self.btns[i].append(btn)
        self.size = size

    def set(self, pram, value):
        for i in range(0,len(self.btns)):
           for j in range(0,len(self.btns[i])):
                self.btns[i][j][pram] = value

    def bind(self,foo):
        for i in range(0,len(self.btns)):
           for j in range(0,len(self.btns[i])):
                self.btns[i][j].bind("<Button-1>", foo)

def btns_disable(btns):
        for i in range(0,len(btns)):
           for j in range(0,len(btns[i])):
                btns[i][j].config(state = 'disabled', relief=SUNKEN, borderwidth=1)

def btns_show(btns,field):
        for i in range(0,len(btns)):
           for j in range(0,len(btns[i])):
                if field.board[i][j] == 1:
                    btns[i][j].config(text = 'Q')
                btns[i][j].config(state = 'disabled', relief=SUNKEN, borderwidth=1)


def newGame():
    global fl
    global my_f
    box2.grid_remove()
    lb2.grid_remove()
    my_f.n_ships = 0
    my_f.reset()
    fl.reset()
    my_btns.set('state','active')
    btns_disable(btns1.btns)
    my_btns.set('text',' ')
    my_btns.set('bg',COLOR)
    btns1.set('text','')
    my_btns.set('relief','raised')
    my_btns.bind(add_ship)
    i = num_of_ships
    while i>0:
        coord = get_rand_coord(size)
        x = coord['x']
        y = coord['y']
        if 1 != fl.board[x][y]:
            fl.board[x][y] = 1
            i-=1


def add_ship(event):
    global my_f
    grid_info = event.widget.grid_info()
    x = int(grid_info["row"])
    y = int(grid_info["column"])
    c = {'x':x, 'y':y}
    my_f.modif(c,1)
    my_btns.btns[x][y].config(state = 'disabled', relief=SUNKEN, borderwidth=1, text=u"\u2714")
    if my_f.n_ships==num_of_ships:
        play()


def play():
    global my_btns
    global fl
    global box2
    global lb2
    box2.grid(row = 2, column = 2)
    lb2.grid(row = 1, column = 2)
    btns_disable(my_btns.btns)
    my_btns.bind(nothing)
    btns1.set('state','active')
    btns1.set('relief','raised')
    btns1.bind(fire)

def nothing(event):
    pass

def fire(event):
    global fl  
    global btns1
    grid_info = event.widget.grid_info()
    x = int(grid_info["row"])
    y = int(grid_info["column"])
    c = {'x':x, 'y':y}
    res = fl.modif(c,2)
    btns1.btns[x][y].config(state = 'disabled', relief=SUNKEN, borderwidth=1)
    btns1.btns[x][y].bind("<Button-1>",nothing)
    if res == 1:
        btns1.btns[x][y].config(text="X")
    bot_fire()
    win = fl.is_empty()
    lose = my_f.is_empty()
    if win:
        pass
    if lose:
        pass
    if win or lose:
        btns_show(btns1.btns,fl)
        btns1.bind(nothing)

def bot_fire():
    c = get_rand_coord(size)
    my_f.modif(c,2)
    x = c['x']
    y = c['y']
    while  my_f.board[x][y]==2 :
            c = get_rand_coord(size)
            x = c['x']
            y = c['y']
    my_f.modif(c,2)
    my_btns.btns[x][y]['bg'] = 'red'
    my_btns.btns[x][y]['text'] = u"\u2622"

root = Tk()
n=4
num_of_ships = 4
size = 5

menubar = Menu(root)
menubar.add_command(label="New Game!", command = newGame)
menubar.add_command(label="Quit!", command=root.quit)
COLOR = root['bg']
root['bg'] = "grey"
box1 = Frame(root,bg="grey")
box2 = Frame(root,bg="grey")
box1.config(borderwidth=5)
box2.config(borderwidth=5)
lb1 = Label(root,text="Ваше поле",bg="grey")
lb2 = Label(root,text="Поле противника",bg="grey")


my_btns = Btns(size,box1) #Add_btns(size,box1)
btns1 = Btns(size,box2) #Add_btns(size,box2)


box1.grid(row = 2, column = 1)
lb1.grid(row = 1, column = 1)
#box2.grid(row = 2, column = 2)
#lb2.grid(row = 1, column = 2)

fl = Field(size)
my_f = Field(size)


# display the menu
root.config(menu=menubar)
root.mainloop()
