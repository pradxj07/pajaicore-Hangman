import random
import string

random_letters = (random.choices(string.ascii_lowercase,k=7))
word = ''
word = word.join(random_letters)

print(word)

def check_guess(guess):
    guess1 = guess.lower() 
    if (guess1 in word):
        print("Good guess! ",guess1 ,"is in the word.")
    else:
        print("Sorry, ",guess1, " is not in the word. Try again.")

def ask_for_input(): 
    while True:
        guess = input("Enter a letter")
        if(len(guess) == 1 and  guess.isalpha() ):
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical acharacter.")
    
    check_guess(guess)
    # return guess


ask_for_input()   

# print(guess)
