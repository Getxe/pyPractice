from random import randint
class Field(object):
    def __init__(self,size):
        self.board = []
        for i in range(size):
            self.board.append([0] * size)
        self.size = size

    def __repr__(self):
        st=''
        for i in range(0,self.size):
            for item in self.board[i]:
                st += str(item)+" "
            st+='\n'
        return st

    def modif(self, c):
        x = c['x']
        y = c['y']
        res = self.board[x][y]
        self.board[x][y] = 2
        return res

    def display(self):
        res = ''
        for i in self.board:
            for itm in i:
                if itm == 2:
                    res+="X "
                else:
                    res+="O "
            res+='\n'
        print res

    def is_end(self):
        for line in self.board:
            if line.count(1)!=0:
                return False
        else:
            return True



def get_user_coord(size):
    y = int(raw_input("Please, input column: "))
    while y<0 or y>size-1:
        y = int(raw_input("This value is incorrect, please, try again: "))
    x = int(raw_input("Please, input row: "))
    while x<0 or x>size-1:
        x = int(raw_input("This value is incorrect, please, try again: "))
    coord = {'x':x,'y':y}
    return coord

def get_rand_coord(size):
    coord = {'x':randint(0,size-1),'y':randint(0,size-1)}
    return coord

def get_coord(size,plr):
    if plr == "r":#computer
        return get_rand_coord(size)
    elif plr == 'i':#human
        return get_user_coord(size)
    else:
        return {'x':-1, 'y':-1 }


"""num_of_ships = 1
size = 5
fl = Field(size)
#random initialization ships
for i in range(0, num_of_ships):
    coord = get_coord(size,'r')
    x = coord['x']
    y = coord['y']
    fl.board[x][y] = 1
i=1
print "Step %s" % i
fl.display()
while(not fl.is_end()):
    c = get_coord(size,'i')
    res = fl.modif(c)
    if res == 2:
        print "We have shooted this coordinates already! Try other coordintes!"
        continue
    elif res == 1:
        print "You hit!"
    else:
        print "You missed."
    i+=1
    print "Step %s" % i
    fl.display()

print "WIN!"""


