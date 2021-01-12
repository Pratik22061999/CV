import random
def drawBoard(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def inputplayer():
    letter = ''
    while not(letter == 'X' or letter =='O'):
        print("Do you want to be X or O?")
        letter = input().upper()
    if letter == 'X':
        return['X','O']
    if letter == 'O':
        return['O','X']
        
def whosefirst():
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'  

def makeMoveboard(board,letter,move):
    board[move] = letter

def iswinner(b,l):
    # board and letter are arguments to check
    # b = board and l = letter
    return( (b[7] == l and b[8] == l and b[9] == l)or
            (b[4] == l and b[5] == l and b[6] == l)or
            (b[1] == l and b[2] == l and b[3] == l)or
            (b[7] == l and b[4] == l and b[1] == l)or
            (b[8] == l and b[5] == l and b[2] == l)or
            (b[9] == l and b[6] == l and b[3] == l)or
            (b[7] == l and b[5] == l and b[3] == l)or
            (b[9] == l and b[5] == l and b[1] == l))
def getBoardCopy(board):
    #making a copy of board list
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board,move):
    return board[move] == ' '

def getplayerMove(board):
    move = ' '
    while (move not in '1 2 3 4 5 6 7 8 9'.split()) or not isSpaceFree(board,int(move)): #short circuit
        print('What is your next move?')
        move = input()
    return(int(move))

def chooseRandomMovefromlist(board,moveslist):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possiblemoves = []
    for i in moveslist:
        if isSpaceFree(board,i):
            possiblemoves.append(i)
    if len(possiblemoves)!= 0:
        return random.choice(possiblemoves)
    else:
        return None

#computer AI
def getcomputermove(board,computerletter):
    if computerletter == 'X':
        playerletter = 'O'
    else:
        playerletter='X'
    #algorithm for tic-tac-toe if the computer can win in the next move
    for i in range(1,10):
        boardcopy = getBoardCopy(board)
        if isSpaceFree(boardcopy,i):
            makeMoveboard(boardcopy,playerletter,i)
            if iswinner(boardcopy,playerletter):
                return i
    # algorithm if player can win in the next move block them
    for i in range(1,10):
        boardcopy = getBoardCopy(board)
        makeMoveboard(boardcopy,playerletter,i)
        if iswinner(boardcopy,playerletter):
            return i
        
    # try to take one of the corners
    move = chooseRandomMovefromlist(board,[1,3,7,9])
    if move!= None:
        return move
    # try to take the center
    if isSpaceFree(board,5):
        return 5
    # try to take sides
    return chooseRandomMovefromlist(board,[2,4,6,8])
def isboardfull(board):
    #checking if the board is full then return true
    
    for i in range(1,10):
        if isSpaceFree(board,i):
            return False
    return True
if __name__=="__main__":
    print("Welcome to the TIC-TAC-TOE")
    while True:
        theboard = [' ']*10
        playerletter,computerletter = inputplayer()
        turn = whosefirst()
        print("The " + turn + ' Will go first.')
        gameplaying = True
        # gameplaying to ensure that game is running
        # running the player turns
        while gameplaying:
            if turn == 'player':
                drawBoard(theboard)
                move = getplayerMove(theboard)
                makeMoveboard(theboard,playerletter,move)
                if iswinner(theboard,playerletter):
                    drawBoard(theboard)
                    print("Hooray you have won the game")
                    gameplaying = False
                else:
                    if isboardfull(theboard):
                        drawBoard(theboard)
                        print("The game is tie")
                        break
                    else:
                        turn = 'computer'
            else:
                # computer turn
                move = getcomputermove(theboard,computerletter)
                makeMoveboard(theboard,computerletter,move)
                if iswinner(theboard,computerletter):
                    drawBoard(theboard)
                    print("The computer is won")
                    gameplaying = False
                else:
                    if isboardfull(theboard):
                        drawBoard(theboard)
                        print("The game is tie")
                        break
                    else:
                        turn = 'player'
        print("Do you want to play again?")
        if not input().lower().startswith('y'):
            break
