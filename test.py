# -*- coding: utf-8; -*-
from Tkinter import *
from bs import *
root = Tk()
num_of_ships = 1
size = 5
fl = Field(size)

def newGame():
    print "Choose pistions of shops"
    for i in btns:
    	for b in i:
    		b.config(state = 'active', relief=RAISED, bg='white',text = 'O')
    		b.bind("<Button-1>", get_coord_g)


	fl = Field(size)
	#random initialization ships
	for i in range(0, num_of_ships):
	    coord = get_coord(size,'r')
	    x = coord['x']
	    y = coord['y']
	    fl.board[x][y] = 1
	print "GOAL :",x,y
	print "FIELD"
	print fl


def  get_coord_g(event):

    grid_info = event.widget.grid_info()
    x = int(grid_info["row"])
    y = int(grid_info["column"])
    c = {'x':y, 'y':x}
    print "coordinates of click",x,y
    res = fl.modif(c)
    print res
    if res == 2:
        print "We have shooted this coordinates already! Try other coordintes!"
    elif res == 1:
        print "You hit!"
    else:
        print "You missed."
	print fl


# create a toplevel menu
menubar = Menu(root)
menubar.add_command(label="Hello!", command=newGame)
menubar.add_command(label="Quit!", command=root.quit)

box = Frame(root)
btns = []
for i in xrange(0,size):
	btns.append([])
	for j in xrange(0,size):
		btn = Button(root,width = 2, text = ' ')
		btn.grid(row = i, column = j)
		btn.config(state = 'disabled',bg='white', relief=SUNKEN, borderwidth=1)
		btns[i].append(btn)



# display the menu
root.config(menu=menubar)
root.mainloop()