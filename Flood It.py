import random
from tkinter import *

root=Tk()

colors=9
cwidth=12
cheight=12
tilesize=40

tcol=0
pastcol=0
count=0

board=[[random.randint(0,colors-1) for j in range(cwidth)] for i in range(cheight)]
win=False

colorlist=["#ff0000","#00ff00","#4040ff","#ffff00","#ff40ff","#00ffff","#009000","#ff9000","#8000c0"]

def start():
    global count,win,board
    board=[[random.randint(0,colors-1) for j in range(cwidth)] for i in range(cheight)]
    win=False
    lbl.config(text="Flood-It")
    count=0
    [[canvas.create_rectangle(j*tilesize,i*tilesize,(j+1)*tilesize,(i+1)*tilesize,fill=colorlist[board[i][j]]) for j in range(cwidth)] for i in range(cheight)]

def turn():
    global tcol,count,pastcol,win
    pastcol=board[0][0]
    if board[0][0]!=tcol:
        board[0][0]=tcol
        flood(0,0)
        [[canvas.create_rectangle(j*tilesize,i*tilesize,(j+1)*tilesize,(i+1)*tilesize,fill=colorlist[board[i][j]]) for j in range(cwidth)] for i in range(cheight)]
        count+=1
        win=True
        for row in board:
            for item in row:
                win=(False if item!=tcol else win)

        lbl.config(text="You win! Your score is "+str(count)+".") if win else nothing()

def flood(row,col):
    global tcol
    board[row][col]=tcol
    for i in range(4):
        r=row+int((complex(0,1)**i).real)
        c=col+int((complex(0,1)**i).imag)
        if not (r==-1 or c==-1 or r==cheight or c==cwidth or board[r][c]==tcol):            
            flood(r,c) if board[r][c]==pastcol else nothing()

def nothing():
    pass

def settcol(event):
    global tcol
    if not (win or int(event.char)>colors+1):
        tcol=int(event.char)-1
        turn()

lbl=Label(root,text="Flood-It",font="Arial "+str(tilesize))
lbl.grid(row=0,column=0)

canvas=Canvas(root,width=(cwidth+1.5)*tilesize,height=max([cheight,colors])*tilesize)
canvas.grid(row=1,column=0)

for i in range(colors):
    canvas.create_rectangle((cwidth+0.5)*tilesize,i*tilesize,(cwidth+1.5)*tilesize,(i+1)*tilesize,fill=colorlist[i])
    canvas.create_text((cwidth+1)*tilesize,(i+0.5)*tilesize,text=str(i+1),font="Arial "+str(int(tilesize/1.5)))

restart=Button(root,text="Restart",command=start)
restart.grid(row=2,column=0,columnspan=cwidth)

root.bind("1",settcol)
root.bind("2",settcol)
root.bind("3",settcol)
root.bind("4",settcol)
root.bind("5",settcol)
root.bind("6",settcol)
root.bind("7",settcol)
root.bind("8",settcol)
root.bind("9",settcol)

[[canvas.create_rectangle(j*tilesize,i*tilesize,(j+1)*tilesize,(i+1)*tilesize,fill=colorlist[board[i][j]]) for j in range(cwidth)] for i in range(cheight)]
              
root.mainloop()

    
