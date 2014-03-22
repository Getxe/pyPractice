from random import randint
class Field(object):
    board = []  #наше поле
    n_ships = 0 #количествл караблей 
    def __init__(self,size):
        for i in range(0, size):
            self.board.append([0] * size)
        self.size = size

    def __repr__(self):
        st=''
        for i in range(0,self.size):
            for item in self.board[i]:
                st += str(item)+" "
            st+='\n'
        return st

    def reset(self):
    #функция сброса расположения караблей
        self.board = []
        for i in range(0, self.size):
            self.board.append([0] * self.size)
        # 0 - пусто
        # 1 - занято
        # 2 - подбито
        # n - на что меняем
    def modif(self, c, n):
    #изменения значения клетки по координатам
        x = c['x']
        y = c['y']
        was = self.board[x][y]
        
        if n == 1 and 0 == was:
            self.n_ships+=1
        elif n == 2 and 1 == was:
            self.n_ships-=1
        
        self.board[x][y] = n
        return was

    def display(self):
        #old---------------------
        res = ''
        for i in self.board:
            for itm in i:
                if itm == 2:
                    res+="X "
                else:
                    res+="O "
            res+='\n'
        print res

    def is_empty(self):
    #проверка на сушествование целых караблей
        for line in self.board:
            if line.count(1)!=0:
                return False
        else:
            return True

def get_user_coord(size):
    """Получение координат с клавиатуры"""
    y = int(raw_input("Please, input column: "))
    while y<0 or y>size-1:
        y = int(raw_input("This value is incorrect, please, try again: "))
    x = int(raw_input("Please, input row: "))
    while x<0 or x>size-1:
        x = int(raw_input("This value is incorrect, please, try again: "))
    coord = {'x':x,'y':y}
    return coord

def get_rand_coord(size):
    """Получение случайных координат"""
    coord = {'x':randint(0,size-1),'y':randint(0,size-1)}
    return coord

def get_coord(size,plr):
    if plr == "r":#computer
        return get_rand_coord(size)
    elif plr == 'i':#human
        return get_user_coord(size)
    else:
        return {'x':-1, 'y':-1}
