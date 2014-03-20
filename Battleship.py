from random import randint
#global 
size = 6
count = 1
#choose mode
def pvp_or_pve():
    n = 0
    while n!=1 and n!=2: 
        n = int(raw_input("Please, input number of players(1 or 2):\n"))
    if n == 1:
    	print "Choosen one player mode"
    else:
    	print "Choosen two player mode"
    return n
##########################################################################    
#Initialization CLASS BATTLESHIP
class Battleship(object):
	ships = [[],[]]
	boards = [[],[]]
	def __init__(self,size,mode,count):
		self.size = size
		self.mode = mode
		self.count = count
		for i in range(0, self.size-1):
			self.boards[0].append("O"*self.size)
		self.boards[1] = self.boards[0]

	def print_board(self,n):
	    for row in self.boards[n-1]:
	        print " ".join(row)

	def append_ships(self):
		print "Please, input coordinates of %s ships." % self.count
		n = 0
		if self.mode == 1:
			for i in xrange(0,self.count):
				self.ships[0].append(get_user_coord(self.size))
				self.ships[1].append(get_rand_coord(self.size))
		else:
			for i in xrange(0,self.count):
				print "First player's ships: \n"
				self.ships[0].append(get_user_coord(self.size))
				print "Second player's ships: \n"
				self.ships[1].append(get_user_coord(self.size))
		print my_board.ships[0][0]
		print my_board.ships[1][0]
##########################################################################
def get_user_coord(size):
	x = int(raw_input("Please, input column: "))
	while x<0 or x>size-1:
		x = int(raw_input("This value incorrect, please, try again: "))
	y = int(raw_input("Please, input row: "))
	while y<0 or y>size-1:
		y = int(raw_input("This value incorrect, please, try again: "))
	coord = [x,y]
	return coord

def get_rand_coord(size):
	coord = [randint(0,size-1),randint(0,size-1)]
	return coord
#########################################################################

#MAIN
print "Welcome to Battleship!"
mode = pvp_or_pve()
my_board = Battleship(size,mode,count)
my_board.append_ships()
my_board.print_board(1)

raw_input()
