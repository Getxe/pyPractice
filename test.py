# -*- coding: utf-8; -*-
from Tkinter import *
from bs import *
root = Tk()
num_of_ships = 1
size = 5

def Add_btns(size):
	global btns
	btns = []
	for i in xrange(0,size):
		btns.append([])
		for j in xrange(0,size):
			btn = Button(root, width = 4, height= 2, text = ' ')
			btn.grid(row = i, column = j)
			btn.config(state = 'disabled', relief=SUNKEN, borderwidth=1)
			btns[i].append(btn)
	return btns

def btns_disable(btns):
        for i in range(0,len(btns)):
           for j in range(0,len(btns[i])):
                btns[i][j].config(state = 'disabled', relief=SUNKEN, borderwidth=1)

def newGame():
    global fl 
    fl = Field(size)
    print "Choose pistions of shops"
    for i in btns:
    	for b in i:
    		b.config(state = 'active', relief=RAISED,text = 'O')
    		b.bind("<Button-1>", get_coord_g)
	#random initialization ships
    for i in range(0, num_of_ships):
    	print i
        coord = get_coord(size,'r')
        x = coord['x']
        y = coord['y']
        fl.board[x][y] = 1

def  get_coord_g(event):
    global fl, btns
    grid_info = event.widget.grid_info()
    y = int(grid_info["row"])
    x = int(grid_info["column"])
    c = {'x':x, 'y':y}
    #print "coordinates of click",x,y
    res = fl.modif(c)
    btns[y][x].config(state = 'disabled', relief=SUNKEN)
    if res == 1:
    	btns[y][x].config(text="X")
        #print "We have shooted this coordinates already! Try other coordintes!"
    #elif res == 1:
        #for i in range(0,len(btns)):
        #   for j in range(0,len(btns[i])):
        #       if i == y and j == x :     	        
        #print "You hit!"
    #else:
      
        #print "You missed."
    if fl.is_end():
    	print "Game over"
    	btns_disable(btns)
	


# create a toplevel menu
menubar = Menu(root)
menubar.add_command(label="Hello!", command=newGame)
menubar.add_command(label="Quit!", command=root.quit)

box = Frame(root)
btns = Add_btns(size)
"""for i in xrange(0,size):
	btns.append([])
	for j in xrange(0,size):
		btn = Button(root, width = 4, height= 2, text = ' ')
		btn.grid(row = i, column = j)
		btn.config(state = 'disabled', relief=SUNKEN, borderwidth=1)
		btns[i].append(btn)"""

# display the menu
root.config(menu=menubar)
root.mainloop()

