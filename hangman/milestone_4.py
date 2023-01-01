import random

class Hangman():
    def __init__(self,word_list,num_lives=5):
        word = random.choice(word_list)

        word_guessed = ['_'] * len(word)
        not_guessed = set(word)
        num_letters = len(not_guessed)
        num_lives = num_lives
        word_list = word_list
        list_of_guesses = []


game = Hangman(['test'])
print(game)
print(type(game))