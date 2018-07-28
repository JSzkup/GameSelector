from random_words import RandomWords
words = RandomWords()

HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

class Hangman:
    def __init__(self, words):
        #  Initializes the game state & selects a secret word

        self.missedLetters = ''
        self.correctLetters = ''
        self.secretWord = words.random_word()
        self.gameIsDone = False

    def displayBoard(self):
        # Displays the current status of the game that is being played

        print(HANGMANPICS[len(self.missedLetters)])
        print()

        print('Missed letters:', end=' ')
        for letter in self.missedLetters:
            print(letter, end=' ')
        print()

        blanks = '_' * len(self.secretWord)

        # replace blanks with correctly guessed letters
        for i in range(len(self.secretWord)):
            if self.secretWord[i] in self.correctLetters:
                blanks = blanks[:i] + self.secretWord[i] + blanks[i+1:]

        # show the secret word with spaces in between each letter
        for letter in blanks:
            print(letter, end=' ')
        print()

    def getGuess(self, already_guessed):
        # Gets the input from the user
        # 
        # Makes sure that the input entered is a letter and
        # the letter entered is not already guessed by the user

        while True:
            print('Guess a letter.')
            guess = input().lower()
            if len(guess) != 1:
                print('Please enter a single letter.')
            elif guess in already_guessed:
                print('You have already guessed that letter. Choose again.')
            elif guess not in 'abcdefghijklmnopqrstuvwxyz':
                print('Please enter a LETTER.')
            else:
                return guess

    def checkWin(self):
        # Returns True if the user has won, False otherwise
        # Checks if the user has correctly guessed the secret word
        
        for i in range(len(self.secretWord)):
            if self.secretWord[i] not in self.correctLetters:
                return False

        print('Yes! The secret word is "{0}"! '
               'You have won!'.format(self.secretWord))

        return True

    def checkLost(self):
        # Returns True if the user has lost, False otherwise. 
        # Alerts the user if all his chances have been used

        if len(self.missedLetters) == len(HANGMANPICS) - 1:
            self.displayBoard()

            missed = len(self.missedLetters)
            correct = len(self.correctLetters)
            word = self.secretWord
            print('You have run out of guesses!')
            print('After {0} missed guesses and {1} correct guesses, '
                   'the word was "{2}"'.format(missed, correct, word))

            return True

        return False

    def run(self):
        # Initialises the game play and coordinates the game activities

        print('''          _    _          _   _  _____ __  __          _   _ 
         | |  | |   /\   | \ | |/ ____|  \/  |   /\   | \ | |
         | |__| |  /  \  |  \| | |  __| \  / |  /  \  |  \| |
         |  __  | / /\ \ | . ` | | |_ | |\/| | / /\ \ | . ` |
         | |  | |/ ____ \| |\  | |__| | |  | |/ ____ \| |\  |
         |_|  |_/_/    \_\_| \_|\_____|_|  |_/_/    \_\_| \_|''')
        print("                         Press enter to start")
        input()

        while not self.gameIsDone:
            self.displayBoard()

            guessedLetters = self.missedLetters + self.correctLetters
            guess = self.getGuess(guessedLetters)

            if guess in self.secretWord:
                self.correctLetters = self.correctLetters + guess
                self.gameIsDone = self.checkWin()
            else:
                self.missedLetters = self.missedLetters + guess
                self.gameIsDone = self.checkLost()

# https://github.com/tomislater/RandomWords