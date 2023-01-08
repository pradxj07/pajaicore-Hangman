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
"input" is an in-built python function takes a string as an arguement and shows the message in console. Also, it allows user to enter any value at the prompt. This value is then returned to the program. Here, it is assigned to the variable guess. 

```python
if(len(guess) == 1 and  guess.isalpha() ):
    print("Good guess!") 
else:
    print("Oops! That is not a valid input.")
```
The above code checks whether guess is a single alphabet and shows appropriate message.  

## Milestone 3
(File name milestone_3.py)
As per instructions, two functions were created.
- check_guess
- ask_for_input

### check_guess
Accepts Argument - guess

This is a _void_ function 
- Converts the argument guess to lower case 
- checks whether the value exists in the global sring variable **word** . if it is present, the message "print("Good guess! ",guess1 ,"is in the word.")" is printed in the console else ""Sorry, ",guess1, " is not in the word. Try again." is printed

### ask_for_input 
Arguments - None 

This is a _void_ function 
- runs a while loop asking for a letter via input function and the input is assigned to variable **guess**.   
-- Every time user enters a value, it is checked to be alphabet and single letter  
-- when valid input has been entered, the while loop breaks
- Outside the while loop, the check_guess function is called with **guess** passed as parameter     


## Milestone 4
(File name milestone_4.py)
As per instructions, class named Hangman is created.
- Attributes: the following atttributes are defined and initilised in the magic method __init__
-- word_guessed 
-- not_guessed 
-- num_letters 
-- num_lives 
-- word_list 
-- word 
-- list_of_guesses 

### Methods 
-- __init__ : magic method over-ridden in the class
-- check_guess: checks whether guess is in the word and marks it accordingly  
-- ask_for_input: gets input from user and check whether it is a single alphabet  

#### __init__ : 
Accepts arguments word_list and num_lives (defaulted to 5, if not provided). The attributes are set as follows - 
-- word_list = set to the value of input word_list
-- word = randomly chosen from word_list
-- word_guessed = ['_'] * len(self.word)
-- not_guessed = contains list of letters not guessed from the word using set
-- num_letters = number of words not guessed yet 
-- num_lives = number of wrong guess allowed before the game finishes
-- list_of_guesses = defaulted to empty list

#### check_guess
Accepts Argument - self(default), guess

This is a _void_ function 
- Converts the argument guess to lower case 
- checks whether the value exists in the global sring variable **word** . if it is present, the message "print("Good guess! ",guess1 ,"is in the word.")" is printed in the console else ""Sorry, ",guess1, " is not in the word. " is printed
- If the letter is in the word, 
-- the list **word_guessed** is updated with the letter in appropriate indices
-- num_letters is reduced by 1
- If the letter is NOT in the word, 
-- num_lives is reduced by 1 
- the guess is added to list_of_guesses

#### ask_for_input 
Arguments - self (default)

This is a _void_ function 
- runs a while loop while num_lives > 0 
-- Asks for a letter via input function and the input is assigned to variable **guess**.   
-- Every time user enters a value, it is checked to be alphabet and single letter  
-- if it is a single alphabet, function check_guess is called by passing the guess 
-- if it is not a single alphabet, message "Invalid letter. Please, enter a single alphabetical character." is printed
-- If the guess is already in the list_of_guesses message is printed "You already tried that letter!"

## Milestone 5
(File name milestone_5.py)

The project was built in 5 milestones 
-- Milestone 2 - In this milestone, I learnt about using in-built python modules like random and python functions like choice, input and data types such as list. Using these, I wrote a code that defines a list of words, choose a randam word from the list, accepts input from the user and checks whether the input is a single letter or not. 

-- Milestone 3 -  In this milestone, I learnt to define my own functions. I was able to organise code written previously in milestone 2 and write my own functions _check_guess_ and  _ask_for_input_. I also learnt to use loops in python to repeatedly run a piece of code 

-- Milestone 4 - In milestone 4, I learnt about object-oriented programming and what are objects and classes. I also learnt about attributes and methonds within a class. Using this concept, I was able to define a class Hangman and define the attributes and methods for it. Some of the methods were created using functions that I created in milestone 3.      

-- Milestone 5 - 
Milestone 5 was the final milestone of the project. Here, I wrote a new independent function that created an instance object of the Hangman class. Further, the function runs a while loop which executes asks_for_input from Hangman object until number of lives zero or the user had guessed all letters in the random word chosen by the game. 