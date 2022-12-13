def printboard(board):
      print(board[1] + '|' + board[2] + '|' + board[3])
      print('-+-+-')
      print(board[4] + '|' + board[5] + '|' + board[6])
      print('-+-+-')
      print(board[7] + '|' + board[8] + '|' + board[9])
      print("\n")


def spaceIsFree(position):
    if board[position] == ' ':
        return True
    else:
        return False      

    
def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printboard(board)
        if (checkDraw()):
            print("Draw!")
            exit()
        if checkForWin():
            if letter == 'X':
                print("Player2 wins!")
                exit()
            else:
                print("Player1 wins!")
                exit()

        return


    else:
        print("Can't insert there!")
        position = int(input("Please enter new position:  "))
        insertLetter(letter, position)
        return


def checkForWin():
     return(
      (board[1] == board[2] and board[1] == board[3] and board[1] != ' ')or
      (board[4] == board[5] and board[4] == board[6] and board[4] != ' ')or
      (board[7] == board[8] and board[7] == board[9] and board[7] != ' ')or
      (board[1] == board[4] and board[1] == board[7] and board[1] != ' ')or
      (board[2] == board[5] and board[2] == board[8] and board[2] != ' ')or
      (board[3] == board[6] and board[3] == board[9] and board[3] != ' ')or
      (board[1] == board[5] and board[1] == board[9] and board[1] != ' ')or
      (board[7] == board[5] and board[7] == board[3] and board[7] != ' ')
  )


def checkDraw():
    for key in board.keys():
         if(board[key]==' ') :
             return True
         return False    



def playerMove():
    position = int(input("Enter the position for 'O':  "))
    insertLetter(player, position)
    return
def compmove():
     position = int(input("Enter the position for 'X':  "))
     insertLetter(bot, position)
     return  

#driver code
board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}
printboard(board)
player ='O'
bot = 'X'

print("Positions are as follow:")
print("1, 2, 3 ")
print("4, 5, 6 ")
print("7, 8, 9 ")
print("\n")

while not checkForWin():
    compmove()
    playerMove()
