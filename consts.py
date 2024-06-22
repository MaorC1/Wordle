from wonderwords import RandomWord

# Create an instance of RandomWords
r = RandomWord()
random_word = r.word(word_min_length=5, word_max_length=5)

DEFAULT_WORDLE_BOARD: list[list[str]] = [
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ']
]
