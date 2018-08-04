from games.gallows import *
from games.noughtsAndCrosses import *

def play_again():
    # Returns True if the player wants to play again, false otherwise

    print()
    print('Do you want to play again? (yes or no)')
    return input().lower() == 'yes'


def main():
    # Main application entry point
    hangman = Hangman(words)
    ticTacToe = TicTacToe()

    game = 0
    while game not in '1 2'.split():
        print("What game would you like to play?")
        print("1. Hangman")
        print("2. Tic-Tac-Toe")
        print()
        game = input("please press the number of the game youd like to play then press enter: ")
    

    if game == 1:
        currentGame = hangman
    else:
        currentGame = ticTacToe

    while True:
        currentGame.run()
        if play_again():
            currentGame.run()
        else:
            break

if __name__ == "__main__":
    main()


# Other Game Ideas
# Chess
# Checkers

# http://patorjk.com/software/taag/