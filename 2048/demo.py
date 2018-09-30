from  random import  randrange,choice

letters=[ord(ch) for ch in 'WASDQRwasdqr']
actions=['Up','Down','Left','Right','Exit','Restart']
actions_dict=dict((zip(letters,actions*2)))


#得到用户的输入 操作
def get_user_action(stdstr):
    char ='N'
    while char not in letters:
        char = stdstr.getchar()
    return actions_dict[char]


def transpose(field):
    return [list(row) for row in zip(*field)]

def invese(field):
    return [row[::-1] for row in field]





class GameField(object):
    def __int__(self,width=4,hight=4,win=32):
        self.width = width
        self.hight = hight
        self.win = win
        self.score = 0
        self.highscore =0

    def reset(self):
        if self.score> self.highscore :
            self.highscore = self.score
        self.score =0
        self.field = [[0 for i in self.width] for j in self.hight]
        self.randomField()
        self.randomField()


    def move(self,direction):
        def move_left(row):
            for i in range(len(row)-1):
                for j in range(i+1,len(row)):
                    if row[j]>0:
                        if row[i] ==0:
                            row[i] = row[j]
                            row[j] = 0
                        if row[i] == row[j]:
                            row[i] = row[i]*2
                            row[j] =0
                            self.highscore = row[i]
            return row


        moves={}

        moves['Left'] =lambda field :[move_left(row) for row in field]

        moves['Right'] = lambda field:[invese(moves['Left'](invese(field)))]

        moves['Up'] = lambda  field:[transpose(invese(moves['Right'](transpose(field))))]

        moves['Down'] =lambda field:[transpose(invese(moves['Left'](transpose(field))))]

        if direction in moves:
            if self.move_is_possible(direction):
                moves[direction]
                self.randomField()
                return True
            else:
                return False


    def draw(self):
        pass

    def is_gameover(self):
        return  not any(self.move_is_possible(direction) for direction in actions )

    def is_win(self):
        return any(any(i>self.win for i in row) for row in self.field)

    #在矩阵中随机位置上随机产生2或者4，
    def randomField(self):
        num = 2 if randrange(100)<90 else 4
        (i,j) =choice([i,j] for i in range(self.width) for j in range(self.hight) if self.field[i][j]>0)
        self.field[i][j] = num

    #在某个方向是否可以移动
    def move_is_possible(self,direction):
        def move_left_is_possible(row):
            def change(i):
                if self.field[i]==0 and self.field[i+1]!=0:
                    return True
                if self.field[i]!= 0 and self.field[i]==self.field[i+1]:
                    return True
            return  any(change(i) for i in range(len(row)))
        moves={}

        moves['Left'] =lambda field:any(move_left_is_possible(row) for row in field)

        moves['Right']= lambda  field:moves['Left'](invese(field))

        moves['Up'] = lambda field:moves['Right'](transpose(field))

        moves['Down'] = lambda field: moves['Left'](transpose(field))

        return moves[direction]


