"""
    ** HangMan **

The plan is that:
    First we generate a random word, make sure that the word is in lowercase
    Generate as many blank as letters in word
    Now ask the user to input a letter
    Here is the if statement:
    If the guessed letter is in the word: Replace the letter with the blank
    Else lose one life
    Here for each state you need to check if the user os out of lifes or the blanks are all full
    If one of the conditions happened game is over else go back and ask for another letter

"""
word_list = ["ranch", "grasp", "camel"]
import random

