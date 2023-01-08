import random

class Hangman():
    def __init__(self,word_list,num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        not_guessed = set(self.word)
        self.num_letters = len(not_guessed)
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
        # self.letterList = list(self.word)

        # self.guess = ''

    def check_guess(self,guess):
        guess1 = guess.lower() 
        if (guess1 in self.word):
            print("Good guess! ",guess1 ,"is in the word.")
            for letterIdx,letter in enumerate(self.word):
                if (letter == guess):
                    self.word_guessed[letterIdx]=letter
                # print(letterIdx)
            self.num_letters -= 1
            print(self.word_guessed, " / ", self.num_letters)
        else:
            self.num_lives -= 1
            print("Sorry, ",guess1, " is not in the word. ")
            print("You have", self.num_lives, "lives left.")

        self.list_of_guesses.append(guess)
        # self.list_of_guesses.append(guess)

    def ask_for_input(self): 
        # while True:
        guess = input("Enter a letter")
        if not(len(guess) == 1 and  guess.isalpha() ):
            # break
        # else:
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
            print(self.list_of_guesses)
        else:  
            self.check_guess(guess) 
    # return guess
def play_game(game_word_list):
    # function 
    game = Hangman(game_word_list,3)
    while True:
        if game.num_lives == 0:
            print("You lost")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else: 
            print("Congratulations. You won the game!")
            break

play_game(["apple","football","mischief","practise","maintain","maintenance","winter","butterfly"])



# print(game.word, game.num_letters)
# print(type(game))
# game.ask_for_input()    i
