import random
import turtle

wn=turtle.Screen()
wn.bgcolor("white")
wn.setup(height=560, width=560)
wn.tracer(0)

class Pen (turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("triangle")
        self.color("black")
        self.speed(0)
##        self.hideturtle()
        
pen=Pen()
pen.goto(-280, 280)
##pen.right(90)
pen.pendown()

for i in range (7):
    for j in range (2):
        pen.forward(80)
        pen.right(90)
        pen.forward(560)
        pen.right(90)
    pen.forward(80)
pen.goto(-280, 280)
pen.right(90)
for i in range (7):
    for j in range (2):
        pen.forward(80)
        pen.left(90)
        pen.forward(560)
        pen.left(90)
    pen.forward(80)


board=[[0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]]

board2=[[0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]]


bomb_num=0
bomb_positions=[]
while bomb_num!=6:
    x=random.randint(0, 6)
    y=random.randint(0, 6)
    if board[x][y]!=9:
        board[x][y]=9
        bomb_num+=1
        bomb_positions.append([x, y])
        
    else:
        pass

##print (board)

for i in (bomb_positions):
##    print (i[0], i[1])
    try:
        if board[i[0]][i[1]+1]!=9:
            board[i[0]][i[1]+1]+=1
    except IndexError:
        pass
    
    try:
        if board[i[0]][i[1]-1]!=9 and i[1]-1>=0:
            board[i[0]][i[1]-1]+=1
    except IndexError:
        pass

    try:
        if board[i[0]+1][i[1]]!=9:
            board[i[0]+1][i[1]]+=1
    except IndexError:
        pass

    try:
        if board[i[0]-1][i[1]]!=9 and i[0]-1>=0:
            board[i[0]-1][i[1]]+=1
    except IndexError:
        pass

    try:
        if board[i[0]+1][i[1]+1]!=9:
            board[i[0]+1][i[1]+1]+=1
    except IndexError:
        pass

    try:
        if board[i[0]+1][i[1]-1]!=9 and i[1]-1>=0:
            board[i[0]+1][i[1]-1]+=1
    except IndexError:
        pass

    try:
        if board[i[0]-1][i[1]+1]!=9 and i[0]-1>=0:
            board[i[0]-1][i[1]+1]+=1
    except IndexError:
        pass

    try:
        if board[i[0]-1][i[1]-1]!=9 and i[0]-1>=0 and i[1]-1>=0:
            board[i[0]-1][i[1]-1]+=1
    except IndexError:
        pass
    


for i in board:
    print (i)



def placement(x, y):
    for i in range (2):
        if i==0:
            num=x
        else:
            num=y
        if i==0:
            column=(round(num/80)+3)
        else:
            row=(round((num*-1)/80)+3)
    print (row, column)
    board2[row][column]=1
            
            
        


wn.listen()
wn.onscreenclick(placement)


while True:
    wn.update()

