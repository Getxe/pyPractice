from random import randint
#global
size = 6
count = 1
#choose mode
def pvp_or_pve():
    n = 0
    while n!=1 and n!=2:
        try:
            n = int(raw_input("Please, input number of players(1 or 2):\n"))
        except:
            pass
    if n == 1:
        print "Choosen one player mode"
    else:
        print "Choosen two player mode"
    return n
##########################################################################
#Initialization CLASS BATTLESHIP
class Battleship(object):
    ships = [[],[]]
    boards = [[],[]]#coords of shoots 1 and 2 palyer
    win = 0
    def __init__(self,size,mode,count):
        self.size = size
        self.mode = mode
        self.count = count
        for i in range(0, self.size-1):
            self.boards[0].append("O"*self.size)
        self.boards[1] = self.boards[0]

    def print_board(self,n):
        print "Field of %s player" % (n+1)
        for row in self.boards[n]:
                print " ".join(row)

    def append_ships(self):
        print "Please, input coordinates of %s ships." % self.count
        n = 0
        if self.mode == 1:
            for i in xrange(0,self.count):
                print "Ship %s" % (i+1)
                self.ships[0].append(get_coord(self.size,'h'))#first player ships
                self.ships[1].append(get_coord(self.size,'c'))#second player ships
        else:
            print "First player's ships: \n"
            for i in xrange(0,self.count):
                print "Ship %s" % (i+1)
                self.ships[0].append(get_coord(self.size,'h'))#first player ships
            print "Second player's ships: \n"
            for i in xrange(0,self.count):
                print "Ship %s" % (i+1)
                self.ships[1].append(get_coord(self.size,'h'))#second player ships

    def fire(self):
        """First shoot take 1 player, Second shoot - 2 player"""
        if self.mode == 1:
            sh1 = get_coord(self.size, 'h')
            sh2 = get_coord(self.size, 'c')
            if self.boards[0][sh1[0]][sh1[1]] == 'O':
                if self.ships[1].count(sh1) == 1:
                    self.ships[1].remove(sh1)
                    self.boards[0][sh1[0]][sh1[1]]='X'
                    print 'x'
                else:
                    self.boards[0][sh1] = change_char(self.boards[0][sh1],'-',sh2)

            else:
                print"You can't fire to this sector again!"
        else:
            pass
            #player's 1 shoot
            #player's 2 shoot

    def check_win():
        """Check if win some player when somebody won returns his number else returns False"""
        pass
#-----------------------------------------------------------------------
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

def get_coord(size,plr):
    if plr == "c":#computer
        return get_rand_coord(size)
    elif plr == 'h':#human
        return get_user_coord(size)
    else:
        return [-1,-1]

def change_char(str,ch,n):
    return str[:n-1]+ch+str[n+1:]
#-----------------------------------------------------------------------

#MAIN
raw_input()
print "Welcome to Battleship!"
mode = pvp_or_pve()
my_board = Battleship(size,mode,count)
my_board.print_board(1)
my_board.append_ships()
my_board.fire()
my_board.print_board(0)


raw_input()
