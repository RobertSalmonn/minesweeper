import random
import turtle

wn=turtle.Screen()
wn.bgcolor("white")
wn.setup(height=560, width=560)
wn.tracer(0)

game_over=False

bombs=[]
class Bomb (turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("circle")
        self.color("red")
        self.speed(0)
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)
        bombs.append(self)

flags=[]
class Flag (turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("square")
        self.color("orange")
        self.speed(0)
        self.shapesize(stretch_wid=1, stretch_len=1.5)
        flags.append(self)

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

num_pen=Pen()
num_pen.hideturtle()

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

g_o_pen=Pen()
g_o_pen.hideturtle()

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


    

def placement(x, y, click):
    global game_over
    
    
    for i in range (2):
        if i==0:
            num=x
        else:
            num=y
        if i==0:
            column=(round(num/80)+3)
        else:
            row=(round((num*-1)/80)+3)
##    print ("pos", row, column)
    
    
    if x<-279 or y>279 or game_over==True:
        pass
    else:
        if click=="left":
            update_board(row, column)
        else:
            place_flag(row, column)
        

def update_board(r, c):
    
    if board2[r][c]==2:
        print ("flag here")
        pass

    else:
        num=(board[r][c])
        


            
        if num==9:
            bomb=Bomb()
            bomb.goto((c*80)-240, (((r*80)-240)*-1))
            loose()

        elif num<9 and num>-1:
            board2[r][c]=1
            num_pen.goto((c*80)-240, (((r*80)-240)*-1)-20)################
            num_pen.write(f"{num}", align="center", font=("Calibri", 30))#putting number into place if picked

    safe=0
    for i in range (7):
        for j in range (7):
            if board2[i][j]==1:
                safe+=1
    if safe==43:
        win()                




            

def place_flag(r, c):
    print (r, c)
    if board2[r][c]==0: #if no flag
        flag=Flag()
        flag.goto((c*80)-240, (((r*80)-240)*-1))#adds flag
        board2[r][c]=2
    elif board2[r][c]==2: #if already flag
        board2[r][c]=0
        for flag in flags:
            if flag.xcor()==(c*80)-240 and flag.ycor()==(((r*80)-240)*-1):
                flag.goto(1000, 1000)
    else:  #if already chosen
        print ("cant go here")

    
def win():
    global game_over
    game_over=True
    print ("winner!")
    g_o_pen.goto(0,0)
    g_o_pen.write(f"YOU WON", align="center", font=("Calibri", 40))
    

def loose():
    global game_over
    game_over=True
    print ("looser")
    g_o_pen.goto(0,0)
    g_o_pen.write(f"YOU LOOSE", align="center", font=("Calibri", 40))
        

def left(x, y):
    placement(x, y, "left")

def right(x, y):
    placement(x, y, "right")
    
            
            
        


wn.listen()
wn.onscreenclick(left)
wn.onscreenclick(right, btn=3)



while True:
    wn.update()

