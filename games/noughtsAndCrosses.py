import random

class TicTacToe():
    def __init__(self):
        # Sets the game state and initializing letter variable

        self.gameIsPlaying = True
        self.letter = ''


    def drawBoard(self, board):
        # The board is a list of 10 strings ignoring 0 to make it 
        # easier on the user when choosing a spot on the board
        print('   |   |')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('   |   |')

    def playerChar(self):
        #player can choose their letter

        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print("Would you like to be X or O?: ")
            letter = input().upper()

        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']
            
    def whoStarts(self):
        if random.randint(0, 1) == 1:
            return 'player'
        else:
            return 'computer'

    def makePlay(self, board, letter, play):
        board[play] = letter
           
    def endConditions(self, board, letter):
        # Given the current board and the players letter, returns true if the player has won

        return ((board[1] == letter and board[2] == letter and board[3] == letter) or # across the top
            (board[4] == letter and board[5] == letter and board[6] == letter) or     # across the middle
            (board[7] == letter and board[8] == letter and board[9] == letter) or     # across the bottom
            (board[1] == letter and board[4] == letter and board[7] == letter) or     # down the left side
            (board[2] == letter and board[5] == letter and board[8] == letter) or     # down the middle
            (board[3] == letter and board[6] == letter and board[9] == letter) or     # down the right side
            (board[1] == letter and board[5] == letter and board[9] == letter) or     # diagonal
            (board[3] == letter and board[5] == letter and board[7] == letter))       # diagonal
        
    def currentBoard(self, board):
        # Duplicating the board list and returning the current board

        currentBoard = []

        for i in board:
            currentBoard.append(i)

        return currentBoard

    def isSpaceFree(self, board, play):
        return board[play] == ' '

    def getTurn(self, board):
        # The players turn

        play =''
        while play not in '1 2 3 4 5 6 7 8 9'.split() or not self.isSpaceFree(board, int(play)):
            print("Numbers 1-9 make up the board")
            print(f"Where would you like to play ({self.letter}): ") # TODO have this show what letter the player currently is
            play = input()

        return int(play)

    def chooseRandomPlayFromList(self, board, alreadyPlayed):
        # Returns a valid move from the pased list on the passed board
        # or returns None if there are no valid moves

        possiblePlays = []
        for i in alreadyPlayed:
            if self.isSpaceFree(board, i):
                possiblePlays.append(i)

        if len(possiblePlays) != 0:
            return random.choice(possiblePlays)
        else:
            return None

    def getCompTurn(self, board, computerLetter):
        # given the current board and the computers letter, determine where to move
        # ************
        # AI algorithm
        # ************
        # Check if the player is about to win
        for i in range(1, 10):
            copy = self.currentBoard(board)
            if self.isSpaceFree(copy, i):
                self.makePlay(copy, computerLetter, i)
                if self.endConditions(copy, computerLetter):
                    return i
        
        # Take the corners if they are free (corners are the key to winning tic tac toe)
        play = self.chooseRandomPlayFromList(board, [1, 3, 7, 9])
        if play != None:
            return play

        # Take the center if free
        if self.isSpaceFree(board, 5):
            return 5

        # Move on sides if the corners and center are taken up
        return self.chooseRandomPlayFromList(board, [2, 4, 6, 8])

    def isBoardFull(self, board):
        # Return True if the board is full

        for i in range(1, 10):
            if self.isSpaceFree(board, i):
                return False
        return True

    def run(self):
        print('''         _______ _          _______             _______         
        |__   __(_)        |__   __|           |__   __|        
           | |   _  ___ ______| | __ _  ___ ______| | ___   ___ 
           | |  | |/ __|______| |/ _` |/ __|______| |/ _ \ / _ \

           | |  | | (__       | | (_| | (__       | | (_) |  __/
           |_|  |_|\___|      |_|\__,_|\___|      |_|\___/ \___|''')
        print("                         Press enter to start")
        print("make sure to change this to input")

        theBoard = [' '] * 10
        playerLetter, computerLetter = self.playerChar()
        turn = self.whoStarts()
        print(f"The {turn} will go first.")

        while self.gameIsPlaying:
            if turn == 'player':
                self.drawBoard(theBoard)
                play = self.getTurn(theBoard)
                self.makePlay(theBoard, playerLetter, play)

                if self.endConditions(theBoard, playerLetter):
                    self.drawBoard(theBoard)
                    print("You Win!")
                    self.gameIsPlaying = False
                else:
                    if self.isBoardFull(theBoard):
                        self.drawBoard(theBoard)
                        print("The game is a tie")
                        break
                    else:
                        turn = 'computer'

            else:
                # Computers turn
                play = self.getCompTurn(theBoard, computerLetter)
                self.makePlay(theBoard, computerLetter, play)

                if self.endConditions(theBoard, computerLetter):
                    self.drawBoard(theBoard)
                    print("You Lose")
                    self.gameIsPlaying = False
                else:
                    if self.isBoardFull(theBoard):
                        self.drawBoard(theBoard)
                        print("The game is a tie")
                        break
                    else:
                        turn = 'player'

