import os
import random

from re import L
winTable = ["x","x","x"]
winTablePC = ["o","o","o"]
board = [[1,2,3],[4,5,6],[7,8,9]]

def pcMove(): #losuje wybrana liczbe i umieszcza ruch przeciwnika
    while True:
        moveX = random.randint(0,2)
        moveY = random.randint(0,2)
        if board[moveX][moveY] != 'x' and board[moveX][moveY] != 'o':
            board[moveX][moveY] = 'o'
            break
        

def drawBoard():
    os.system('clear')
    for i in range(3):
        print(board[i])

def signX():
    area = float(input(":"))
    for i in range(3):
        for j in range(3):
            if board[i][j] == area:
                board[i][j] = "x"

def checkX(): #sprawdza poziome wartosci tabeli czy w pionie sa 3 takie same znaki
    for i in range(3):
        if board[i] == winTable:
            print("U Win!")
            exit()
        elif board[i] == winTablePC:
            print("PC Win!")
            exit()
    
def checkZ(): #sprawdza X czy po skosach sa takie same znaki
    isItx = 0;
    for i in range(3):
        if board[i][i] == winTable[i]:
            isItx +=1
        if isItx == 3:
            print("Win!")
            exit()

    isItx = 0
    for j in range(2,0, -1):
        for i in range(3):
            if board[i][j]== "x":
                isItx +=1
                print(isItx)
                j -=1
            else:
                break
            if isItx == 3:
                print("Win!")
                exit()
            
     
    

         
def checkY(): #sprawdza pionowe słupki tabeli w weryfikacji czy w linii Y sa 3 takie same znaki
    isItx = 0
    for i in range(3):
        for j in range(3):
            if board[j][i] == 'x':
                isItx += 1
            if isItx == 3:
                print("Win!")
                exit()
        isItx = 0

for i in range(9):
    drawBoard()
    signX()
    pcMove()
    drawBoard()
    checkX()
    checkY()
    checkZ()

    
    

