import random

word_list = ["apple", "mango", "clementines", "grapes", "banana"]

word = random.choice(word_list)    

print(word_list)
# print(type(word_list))
print(word)

guess = input("Enter a single letter")

if len(guess) == 1 and guess >= 'a' and guess <='z':
    print("Good guess")
else: 
    print("Oops! That is not a valid input.")