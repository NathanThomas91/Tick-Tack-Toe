from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from PIL import ImageTk, Image

count=0
board=[['','','',],
 ['','','',],
 ['','','',]]
t1=Tk()
t1.geometry("700x600")

def start_window():
    global player1_name, player2_name
    img = ImageTk.PhotoImage(Image.open("bg.jpg"))
    imglabel = Label(t1, image=img, width = 994, height =989)
    imglabel.image = img
    imglabel.place(x=0, y = 0)
    t1.title("TIC TAC TOE")
    l = Label(t1, text = 'Tic Tac Toe Game', font = ('COMIC SANS MS',25,'bold')).place(x=0, y=5)
    l1 = Label(t1, text = 'Enter player 1 name :-', font = ('',20,'')).place(x =0, y = 60)
    l2 = Label(t1, text = 'Enter player 2 name :-', font = ('',20,'')).place(x = 0, y = 100)
    player1_name = Entry(t1, width = 30)
    player2_name = Entry(t1, width = 30)
    player1_name.place(x = 310, y = 70)
    player2_name.place(x = 310, y = 110)

    start=Button(t1,text="Start Play",font=('Times',15,'bold'),command=TicTacToeGUI)
    start.place(x = 300, y = 220)

def TicTacToeGUI():
    global t
    t = Toplevel(t1)
    t.geometry("700x600")
    t.title("TIC TAC TOE")
    t.grab_set()
    global player1_name, player2_name
    exitButton=Button(t,text="Quit",command=Quit,font=("COMIC SANS MS",10,"bold"))
    exitButton.place(x = 100, y = 400)
    # i have a error here on calling the function
    b1=Button(t,text="",font=('Times',15,'bold'),command =lambda: changeVal(b1,0,0))
    b2=Button(t,text="",font=('Times',15,'bold'),command =lambda: changeVal(b2,0,1))
    b3=Button(t,text="",font=('Times',15,'bold'),command =lambda: changeVal(b3,0,2))
    b4=Button(t,text="",font=('Times',15,'bold'),command =lambda: changeVal(b4,1,0))
    b5=Button(t,text="",font=('Times',15,'bold'),command =lambda: changeVal(b5,1,1))
    b6=Button(t,text="",font=('Times',15,'bold'),command =lambda: changeVal(b6,1,2))
    b7=Button(t,text="",font=('Times',15,'bold'),command =lambda: changeVal(b7,2,0))
    b8=Button(t,text="",font=('Times',15,'bold'),command =lambda: changeVal(b8,2,1))
    b9=Button(t,text="",font=('Times',15,'bold'),command =lambda: changeVal(b9,2,2))
    b1.place(x =230, y =220)
    b2.place(x =310, y =220)
    b3.place(x =380, y =220)
    b4.place(x =235, y =270)
    b5.place(x =315, y =270)
    b6.place(x =380, y =270)
    b7.place(x =235, y =330)
    b8.place(x =315, y =330)
    b9.place(x =380, y =330)
    board1 = Label(t, text = '____________________', font = ('',15,'')).place(x =205, y =250)
    board2 = Label(t, text = '|', font = ('',30,'')).place(x =275, y =230)
    board3 = Label(t, text = '|', font = ('',30,'')).place(x =350, y =230)
    board4 = Label(t, text = '|', font = ('',30,'')).place(x =275, y =280)
    board5 = Label(t, text = '|', font = ('',30,'')).place(x =350, y =280)
    board6 = Label(t, text = '|', font = ('',30,'')).place(x =275, y =330)
    board7 = Label(t, text = '|', font = ('',30,'')).place(x =350, y =330)
    board8 = Label(t, text = '____________________', font = ('',15,'')).place(x =205, y =300)

def changeVal(button,boardValRow,boardValCol):
    global count, player1_name, player2_name, p1, p2
    p1 = player1_name.get()
    p2 = player2_name.get()
    if button["text"] == "":
        if count%2 == 0:
            button["text"]="X"
            m="PLAYER: %s(x)" % (p2)
            l1=Label(t,text=m ,height=3,font=("COMICSANS MS",10,"bold")).place(x = 40, y = 130)
            board[boardValRow][boardValCol]="X"
        else:
            button["text"] = "O"
            m1="PLAYER: %s(O)" % (p1)
            l1=Label(t,text=m1,height=3,font=("COMICSANS MS",10,"bold")).place(x = 40, y = 130)
            board[boardValRow][boardValCol] = "O"
        count=count+1
        if count>=5:
            checkWinner()
    else:
        messagebox.showerror("Error","This box already has a value!")
        
def checkWinner():
    global count,board
    if (board[0][0] == board[0][1] == board[0][2] == "X" or board[1]
        [0] == board[1][1] == board[1][2] == "X" or board[2][0] == board[2]
        [1] == board[2][2] == "X" or board[0][0] == board[1][0] == board[2]
        [0] == "X" or board[0][1]== board[1][1] == board[2][1] == "X" or 
        board[0][2] == board[1][2] == board[2][2] == "X" or
        board[0][0] == board[1][1] == board[2][2] == "X" or board[0]
        [2] == board[1][1] == board[2][0] == "X"):
            m ="Player %s" % (p2)
            displayWinner(m)
    elif (board[0][0] == board[0][1] == board[0][2] == "O" or board[1]
          [0] == board[1][1] == board[1][2] == "O" or board[2][0]     
           == board[2][1] == board[2][2] == "O" or
          board[0][0] == board[1][0] == board[2][0] == "O" or board[0]  
          [1] == board[1][1] == board[2][1] =="O" or board[0]
          [2] == board[1][2] == board[2][2] =="O" or board[0]
          [0] == board[1][1] == board[2][2] == "O" or board[0]
          [2] == board[1][1] == board[2][0] == "O"):
            m1="Player %s" % (p1)
            displayWinner(m1)
    elif count == 9:
        displayWinner("NONE! IT IS A TIE!")

def displayWinner(winner):
    global t,winnerWindow    
    winnerWindow = Tk()
    winnerWindow.title("Winner")
    l1 = Label(winnerWindow,text = "THE WINNER IS: ",font = ("COMIC SANS MS",15,''))
    l1.pack()
    l2 = Label(winnerWindow,text = winner,font = ("COMIC SANS MS",15,''))
    l2.pack()
    gameover=Button(winnerWindow,text = "Exit",font = ("COMIC SANS MS",10,"bold"),command = destruct)
    gameover.pack()

def destruct():
 global t,winnerWindow
 t.destroy()
 winnerWindow.destroy()

def Quit():
 global t 
 msg=simpledialog.askstring("Quit","Are you want to Quit?",
                            parent = t)
 if msg == 'yes':
     t.destroy()

start_window()
