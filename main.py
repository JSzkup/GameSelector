from games.gallows import *

def play_again():
    # Returns True if the player wants to play again, false otherwise

    print('Do you want to play again? (yes or no)')
    return input().lower() == 'yes'


def main():
    # Main application entry point

    # TODO make this work with more than just hangman
    # print("What game would you like to play?")
    # print("1. Hangman")
    # print("2. Tic-Tac-Toe")
    # print()
    # game = input("please press the number of the game youd like to play then press enter: ")
    # 
    # if game == 1:
    #     current_game = Hangman(words)
    # elif game == 2:
    #     current_game = TicTacToe()

    current_game = Hangman(words)

    while True:
        current_game.run()
        if play_again():
            current_game = Hangman(words)
        else:
            break

if __name__ == "__main__":
    main()


# Other Game Ideas
# Chess
# Checkers