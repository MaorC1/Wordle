from consts import DEFAULT_WORDLE_BOARD, random_word
from color_letters import TextStyle
import enchant
import string


class Wordle:
    def __init__(self):
        self.board = DEFAULT_WORDLE_BOARD
        self.guess_count = 0
        self.word_to_guess = random_word
        self.guessed_words = []
        self.word_dictionary = enchant.Dict("en_US")

    def display_board(self):
        # Create an empty Wordle board (5x5 grid)
        # Print top border
        print("+" + "---+" * len(self.board[0]))

        # Print each row of the board
        for row in self.board:
            print("| " + " | ".join(row) + " |")
            print("+" + "---+" * len(self.board[0]))

    def append_new_word(self, word: str) -> None:
        # replace the empty row with the row of the new word
        colored_word = self.compare_words(word)
        self.board[self.guess_count] = colored_word

    def validate_word(self, word: str):
        flag = True
        error_msg = ''

        # if the word has digits in it
        if any(char.isdigit() for char in word):
            error_msg = "WORD COULD NOT HAVE DIGITS! TRY AGAIN!"
            flag = False

        # check for no special characters and whitespace
        if any(char in string.punctuation + string.whitespace for char in word):
            error_msg = "NO SPECIAL CHARACTERS OR WHITESPACE IN WORD! TRY AGAIN!"
            flag = False

        # if the word is longer then 5 letters
        if len(word) != 5:
            error_msg = "WORD COULD NOT BE LONGER THEN 5 LETTERS! TRY AGAIN!"
            flag = False

        if not self.word_dictionary.check(word):
            error_msg = "NOT A REAL WORD! TRY AGAIN!"
            flag = False

        if word in self.guessed_words:
            error_msg = "CAN'T GUESS THE SAME WORD TWICE! TRY AGAIN!"
            flag = False

        colored_error = TextStyle.color_letter(error_msg, 'red', is_bold=True)
        print(colored_error)
        return flag

    def begin_round(self, word_guess):
        is_valid_word = self.validate_word(word_guess)
        self.guessed_words.append(word_guess)
        if is_valid_word:
            self.append_new_word(word_guess)
            self.display_board()
            self.guess_count += 1

    def check_win(self, word: str):
        if word == self.word_to_guess:
            print(f"CONGRATS!! the word was: {self.word_to_guess}")
            return True

    def compare_words(self, my_guess: str):
        new_lst = []
        for index, letter in enumerate(my_guess):
            if letter in self.word_to_guess:
                if letter == self.word_to_guess[index]:
                    letter = TextStyle.color_letter(letter, 'green', is_bold=True)
                else:
                    letter = TextStyle.color_letter(letter, 'yellow', is_bold=True)
            new_lst.append(letter)
        return new_lst

    def start_game(self):
        # display default board (empty board)
        self.display_board()
        word_guess = input("Guess a word: ")
        game_won = self.check_win(word_guess)
        self.begin_round(word_guess)
        while self.guess_count != 5 and not game_won:
            word_guess = input("Guess a word: ")
            self.begin_round(word_guess)
            game_won = self.check_win(word_guess)
        print(TextStyle.color_letter(f"GAME ENDED! The word was: {self.word_to_guess}", 'blue', True))


if __name__ == "__main__":
    wordle = Wordle()
    wordle.start_game()
