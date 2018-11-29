
   #Game of life

import random
import time

# import only system from os 
from os import system, name 
  

  
# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls')

size = int(input("Insert the size of the square: "))

board = []

def Board(size):
    for i in range(0 , size):
        board.append([])
        for j in range(0 , size):
            board[i].append(0)
    return board


def Draw(z , l):
    out = " "
    for x in range(0 , l):
        out += "__"
    out += "\n"
    for y in range(0,l):
        out += "|"
        for x in range(0,l):
            if z[y][x] == 0:
                 out += "  "
            elif z[y][x] == 1:
                out += "██"
            else:
                out += "  "
        out += "|"
        out += "\n"
    out += " "
    for x in range(0 , l):
        out += "‾‾"
    print(out)

print("Insert the number of starting living cells: ")
start = int(input(""))


t = True
while t == True:
    board = Board(size)
    for i in range(0 , start):
        board[random.randint(0 , size - 1)][random.randint(0 , size - 1)] = 1
    Draw(board , size)
    print("Do you want to proceed with this sample (y/n)?")
    l = input("")
    if l != 'n':
        t = False


gen = 0        
t = True
while t:
    clear()
    Draw(board , size)
    for y in range(0 , size):
        for x in range(0 , size):
            if board[y][x] == 1:
                neighbor = -1
            else:
                neighbor = 0
            for i in range(y - 1 , y + 2):
                for j in range(x - 1 , x + 2):
                    if i >= 0 and j >= 0 and i < size and j < size:
                        if board[i][j] == 1 or board[i][j] == -1:
                                neighbor += 1
            
            if board[y][x] == 1 and not(neighbor == 2 or neighbor == 3):
                board[y][x] = -1
            if board[y][x] == 0 and  neighbor == 3:
                board[y][x] = 2
    
    print("Generation : " , gen)
    gen += 1

            
   
    for y in range(0 , size):
        for x in range(0 , size):
            if board[y][x] == -1:
                board[y][x] = 0
            if board[y][x] == 2:
                board[y][x] = 1
    time.sleep(.2)
