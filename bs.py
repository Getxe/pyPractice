from random import randint
class Field(object):
    def __init__(self,size):
        #self.board = [0] * size
        #for i in range(size):
        #    self.board[i] = [0] * size
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
        self.board[1][y] = 2
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
            if line.count(3)==1:
                return True
        else:
            return False


def get_user_coord(size):
    x = int(raw_input("Please, input column: "))
    while x<0 or x>size-1:
        x = int(raw_input("This value incorrect, please, try again: "))
    y = int(raw_input("Please, input row: "))
    while y<0 or y>size-1:
        y = int(raw_input("This value incorrect, please, try again: "))
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

"""fl = Field(4)
print fl
print fl.is_end()
fl.board[3][3]=3
print fl
print fl.is_end()"""


