import random

class TicTacToe():
    def __init__(self):
        print("INIT")
        #initiate the program

    def displayBoard(board):
        print('   |   |')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('   |   |')

    def startingMove():
        if random.randint(0, 1) == 1:
            return 'player'
        else:
            return 'comp'

    def getTurn(self, already_played):
        while True:
            print("Where would you like to play (X)")
            play = input()
            if len(play) != 1:
                print('Please enter a single number.')
            elif play in already_played: # TODO make sure spots on the board are taken up with this variable once played
                print('That spot is not empty. Choose again.')
            elif play not in '0123456678':
                print('Please enter a NUMBER.')
            else:
                return play

    def aiTurn(self, already_played):
        while True:
            aiPlay = random.randint(0,9)
            if aiPlay in already_played:
                aiPlay = random.randint(0,9) # TODO make sure this actually loops until it gets one thats not already played
            else:
                return aiPlay
            
    def makeMove(board, letter, play, aiplay):
        board[move] = letter
           
    def endConditions(ecks, ohs):
        return ((ohs[7] == ecks and ohs[8] == ecks and ohs[9] == ecks) or # across the top
            (ohs[4] == ecks and ohs[5] == ecks and ohs[6] == ecks) or     # across the middle
            (ohs[1] == ecks and ohs[2] == ecks and ohs[3] == ecks) or     # across the bottom
            (ohs[7] == ecks and ohs[4] == ecks and ohs[1] == ecks) or     # down the left side
            (ohs[8] == ecks and ohs[5] == ecks and ohs[2] == ecks) or     # down the middle
            (ohs[9] == ecks and ohs[6] == ecks and ohs[3] == ecks) or     # down the right side
            (ohs[7] == ecks and ohs[5] == ecks and ohs[3] == ecks) or     # diagonal
            (ohs[9] == ecks and ohs[5] == ecks and ohs[1] == ecks))       # diagonal


    def checkLost():

        return False

    def run(self):
        print('''         _______ _          _______             _______         
        |__   __(_)        |__   __|           |__   __|        
           | |   _  ___ ______| | __ _  ___ ______| | ___   ___ 
           | |  | |/ __|______| |/ _` |/ __|______| |/ _ \ / _ \

           | |  | | (__       | | (_| | (__       | | (_) |  __/
           |_|  |_|\___|      |_|\__,_|\___|      |_|\___/ \___|''')
        print("                         Press enter to start")
        input()

        while not self.gameIsDone:
            self.displayboard()


def main():
    current_game = TicTacToe()

    while True:
        current_game.run()
        if play_again():
            current_game = TicTacToe(words)
        else:
            break

if __name__ == "__main__":
    main()





# https://inventwithpython.com/chapter10.html
# https://codereview.stackexchange.com/questions/108738/python-tic-tac-toe-game
# http://patorjk.com/software/taag/