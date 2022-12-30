# pajaicore-Hangman
hangman using python 
## Milestone 2
This milestone is about being able to use basic variables, functions in python to start the hangman project. The purpose of this milestone was to build a piece of code that will 
- define a list of words, 
- randomly select a word from the list, 
- show console message asking user to enter a letter, 
- accept input from the user, 
- verify whether the input is a single letter
- show console message accordingly.   

the code is saved in file called milestone_2.py. Following is the description of different parts of the code - 
```python
import random
```
Import command is used to include a module that contains a group of inbuilt python functions. In this case, the name of the module is "random". It contains "choice" function which will be used in the code 

```python
word_list = ['apple','papaya','grapes','peach','mango']
print(word_list)
```
word_list is variable that has been assigned a list. the list itself is a collection of objects, here strings. Print command is used to shwo the word list on the screen

```python
word = random.choice(word_list)
print (word)
```
Word is another variable that is assigned a randomly chosen value from the list defined above with the help of choice function.
Again, print is used to show the chosen word in the console. 

guess = input('Enter single letter ')
guess is a variable that is assigned a user-entered value. "input" function enters the 

if(len(guess) == 1 and  guess.isalpha() ):
    print("Good guess!") 
else:
    print("Oops! That is not a valid input.")
```
