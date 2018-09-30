import random

score = 0

matix = [[0 for i in range(4)] for i in range(4)]

def notzero(s):
    return s if s != 0 else ''

def display():
    print("\r\
          ┌──┬──┬──┬──┐\n\
          │%4s│%4s│%4s│%4s│\n\
          ├──┬──┬──┬──┤\n\
          │%4s│%4s│%4s│%4s│\n\
          ├──┬──┬──┬──┤\n\
          │%4s│%4s│%4s│%4s│\n\
          ├──┬──┬──┬──┤\n\
          │%4s│%4s│%4s│%4s│\n\
          └──┴──┴──┴──┘"
          % (notzero(matix[0][0]), notzero(matix[0][1]), notzero(matix[0][2]), notzero(matix[0][3]),
             notzero(matix[1][0]), notzero(matix[1][1]), notzero(matix[1][2]), notzero(matix[1][3]),
             notzero(matix[2][0]), notzero(matix[2][1]), notzero(matix[2][2]), notzero(matix[2][3]),
             notzero(matix[3][0]), notzero(matix[3][1]), notzero(matix[3][2]), notzero(matix[3][3]),)
          )

def init():
    global  score

    score =0
    #matix = [[0 for i in range(4)] for i in range(4)]
    initNumFlag = 0
    while 1 :
        k = 2 if random.randrange(0,20) >0 else 4
        s = divmod(random.randrange(0,16),4)
        if matix[s[0]][s[1]] == 0:
            matix[s[0]][s[1]]= k
            initNumFlag +=1
            if initNumFlag ==2:
                break
    display()


def addRandomNum():
    while 1:
        k =2  if random.randrange(1,10)>1 else 4
        s = divmod(random.randrange(0,16),4)
        if matix[s[0]][s[1]] == 0:
            matix[s[0]][s[1]] =k
            break
    display()




def is_over():
    for i in range(4):
        for j in range(3):
            if matix[i][j]==0 or matix[i][j]== matix[i][j+1] or matix[j][i] ==matix[j+1][i]:
                return False
    return True

def moveRight():
    global score
    for i in range(4):
        for j in range(3,0,-1):
            for k in range(j-1,-1,-1):

                if matix[i][k]>=0:
                    if matix[i][j] == 0:
                        matix[i][j] =matix[i][k]
                        matix[i][k] =0
                    elif matix[i][j] == matix[i][k]:
                        matix[i][j] = 2*matix[i][j]
                        matix[i][k] = 0 ;
                        score+=matix[i][j]
                        break


    addRandomNum()

def moveLeft():
    global  score
    for i in range(4):
        for j in range(3):
            for k in range(j+1,4):
                if matix[i][k]>0:
                    if matix[i][j] == 0:
                        matix[i][j]=matix[i][k]
                        matix[i][k] = 0
                    elif matix[i][j] ==matix[i][k]:
                        matix[i][j] = matix[i][j]*2
                        score += matix[i][j]
                        matix[i][k] = 0
                        break
    addRandomNum()



def moveUp():
    global  score
    for i in range(4):
        for j in range(3):
            for k in range(j+1,4):
                if matix[k][i]>0:
                    if matix[j][i] ==0 :
                        matix[j][i] = matix[k][i]
                        matix[k][i] =0
                    elif matix[j][i] == matix[k][i]:
                        matix[j][i] = matix[j][i]*2
                        score += matix[j][i]
                        matix[k][i] =0
                    break
    addRandomNum()

def moveDown():
    global  score
    for i  in range(4):
        for j in range(3,0,-1):
            for k in range(j-1,-1,-1):
                if matix[k][i] > 0:
                    if matix[j][i] == 0 :
                        matix[j][i] = matix[k][i]
                        matix[k][i] = 0
                    if matix[k][i] == matix[j][i] :
                        matix[j][i] = 2*matix[j][i]
                        matix[k][i] =0
                        score+= matix[j][i]
                    break
    addRandomNum()

def main():
    global matix
    print("    Welcome to the Game of 2048!")
    flag = True
    init()
    while flag:
        print(" you Socre is %s " %(score))
        d = input("W(up),s(down),a(left),d(right),q(quit),r(restart)")
        if d =='w':
            moveUp()
            if is_over():
                print("game over")
                break

        elif d =='s':
            moveDown()
            if is_over():
                print("game over")
                break

        elif d =='a':
            moveLeft()
            if is_over():
                print("game over")
                break

        elif d =='d':
            moveRight()
            if is_over():
                print("game over")
                break

        elif d == 'r':
            matix = [[0 for i in range(4)] for i in range(4)]
            init()

        elif d =='q':
            break
        else:pass

if __name__ == '__main__':
    main()





