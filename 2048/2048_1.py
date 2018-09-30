import curses
from random import randrange, choice # generate and place new tile
from collections import defaultdict

letter_codes =[ord(ch) for ch in 'wasdqrWASDQR']

actions =['Up','Down','Left','Right','Restart','Exit']

actions_dict = dict(zip(letter_codes,actions*2))

#得到用户的输入
def getUserAction(keyboard):
    char = 'N'
    while char not in actions_dict:
        char = keyboard.getch()
    return actions_dict[char]

def transpose(field):
    return [list(row) for row in zip(*field)]

def invert(field):
    return [row[::-1] for row in field]



class GameField(object):
    def __init__(self,height=4,width=4,win =2048):
        self.height = height
        self.width = width
        self.win_value = win
        self.score = 0
        self.hignscore = 0
        self.reset()

    #重置棋盘
    def reset(self):
        if self.hignscore<self.score:
            self.hignscore = self.score
        self.score =0
        #重置矩阵
        self.field = [[0 for i in range(self.width)] for j in range(self.height)]
        randomField()
        randomField()
        pass

    def move(self,direction):
        def move_row_left(row):
            for i in range(len(row)-1):
                for j in range(i+1,len(row)):
                    if row[j]>0:
                       if row[i]==0:
                           row[i] =row[j]
                           row[j] =0
                       elif row[i] == row[j]:
                           row[i] = row[i]*2
                           row[j] =0
                           self.score=row[i]

        moves={}
        moves['Left']= lambda field:[move_row_left(row) for row in field]
        moves['Right'] =lambda field:[invert(moves['left'](invert(field)))]
        moves['Up']=lambda  field:[transpose(moves['Left'](transpose(field)))]
        moves['Down'] =lambda  field:[transpose(moves['Right'](transpose(field)))]

        if direction in moves:
            if self.move_is_possible(direction):
                self.field = moves[direction](self.field)
                self.randomField()
                return True
            else:
                return False






    def is_win(self):
        return any(any(i>self.win_value for i in row) for row in self.field)


    def is_gameover(self):
        return not any(self.move_is_possible(move) for move in actions)


    def draw(self,screen):
        help_string1 ="W(up),S(Down),A(Left),D(Right)"
        help_string2 ="Q(quit),R(Restart)"
        gameove_string="       GAME OVER "
        win_string="    you win "

        def cast(string):
            screen.addstr(string+"\n")

        def draw_hor_separator():
            line ='+'+('+------'*self.width+'+')[1:]
            cast(line)

        def draw_data(row):
            cast("".join("|{:^5} ".format(num) if num>0 else "|      " for num in row)+"|")

        screen.clear()

        cast("Score:"+str(self.score))
        if 0!=self.height:
            cast("Highsocre:"+self.hignscore)
        for row in self.field:
            draw_hor_separator()
            draw_data(row)
        draw_hor_separator()
        if self.is_win():
            cast(win_string)
        else:
            if self.is_gameover():
                cast(gameove_string)
            else:
                cast(help_string1)
        cast(help_string2)





    #在矩阵中随机生成2或者4
    def randomField(self):
        new_num = 4 if randrange(100)>89 else 2
        (i,j) =choice([i,j] for i in range(self.width) for j in range(self.height) if self.field[i][j]==0)
        self.field[i][j] = new_num

    def move_is_possible(self,direction):
        def row_left_movable(row):
            def change(i):
                if row[i]==0 and row[i+1]!=0:
                    return true
                if row[i] !=0 and row[i+1] == row[i]:
                    return true
            return any(change(i) for i in range(len(row)-1))

        check ={}
        check['Left'] = lambda field:any(row_left_movable(row) for row in field)
        check['Right'] = lambda field:check['left'](invert(field))
        check['Up'] = lambda field:check['Left'](transpose(field))
        check['Down'] = lambda field:check['Right'](transpose(field))

        if direction in self.check:
            return check[direction](self.field)
        else:return False


def main(stdscr):

    def init():
        game_field.reset()
        return 'Game'

    def not_game(state):
        game_field.draw(stdscr)

        action = getUserAction(stdscr)

        response = defaultdict(lambda :state)

        response['Restart'],response['Exit'] ='Init','Exit'

        return response[actions]

    def game():
        game_field.draw(stdscr)

        action = getUserAction(stdscr)

        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'
        if game_field.move(action):
            if game_field.is_win():
                return 'Win'
            if game_field.is_gameover():
                return 'Gameover'
        return 'game'

    state_actions={
        'Init':init,
        'Win':lambda :not_game('Win'),
        'Gameover':lambda :not_game('Gameover'),
        'Game':game
    }
    course.use_default_clors()
    game_field = GameField(win=2048)

    state ='Init'
    while state != 'Exit':
        state = state_actions[state]()








