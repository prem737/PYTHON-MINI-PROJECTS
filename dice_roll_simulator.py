#importing the random labrary to use randint function
import random

#by using try and except block we can avoid user input errors
try:
    max_value = int(input("enter the maximum value of dice\n"))
    min_value = int(input("enter the minimum value of dice\n"))
except:
    print("invalid input, program will revert to defaults")
    min_value=1
    max_value=6
    
again = True

while again:
    Dice=random.randint(min_value,max_value)
    print("DICE:",Dice)
    another_roll=input("want to roll the dice again\n")
    if another_roll.lower()=="yes" or another_roll.lower()=="y" :
        again=True
    else:
        again=False

