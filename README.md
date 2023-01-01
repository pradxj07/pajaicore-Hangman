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
