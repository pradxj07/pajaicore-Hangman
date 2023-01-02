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

        # self.guess = ''

    def check_guess(self,guess):
        guess1 = guess.lower() 
        letterList = list(self.word)
        if (guess1 in self.word):
            print("Good guess! ",guess1 ,"is in the word.")
            for letterIdx,letter in enumerate(self.word):
                if (letter == guess):
                    self.word_guessed[letterIdx]=letter
                print(letterIdx)
            self.num_letters -= 1
            print(self.word_guessed, " / ", self.num_letters)

        # else:
        #     print("Sorry, ",guess1, " is not in the word. Try again.")

    def ask_for_input(self): 
        while self.num_letters > 0:
            guess = input("Enter a letter")
            if not(len(guess) == 1 and  guess.isalpha() ):
                # break
            # else:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:  
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                print(self.list_of_guesses)
    # return guess

game = Hangman(['test','ice','dawn','drift','doodle'])
print(game.word, game.num_letters)
# print(type(game))
game.ask_for_input()    