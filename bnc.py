from random import randint
from tkinter import Y
from turtle import end_fill

roles = ["Bear", "Ninja","Cowboy"]
computer = roles[randint(0,2)]
player =False

#Here is the game "Welcome" message:
print("Grr, Hi-ya, Yeehaw! Welcome to Bear, Ninja, Cowboy!")

print() #added for space between strings

#Instructions message with options of y or n
instructions = input("Would you like instructions on how to play? (y/n)")
if instructions == "y":
    print("Bear, Ninja,Cowboy is a fun variation of Rock, Paper, Scissors! Battle it out against the computer by choosing either Bear, Ninja or Cowboy. Bear eats Ninja, Ninja defeats Cowboy and Cowboy shoots bear. ")
else: instructions =="n"
print() #added for space between strings
print("Ok, let's battle!")

#Game play Loop:
print() #added for space between strings
player = False

while player == False:
    
    player = input("Bear, Ninja, or Cowboy?:  ")
    if computer == player.lower():
      print("DRAW!")
    elif computer == "Cowboy":
      if player.lower() == "Bear":
        print("You lose!", computer, "shoots", player)
      else: # computer is cowboy, player is ninja
        print("You win!", player, "defeats", computer)
    elif computer == "Bear":
      if player.lower() == "Cowboy":
        print("You win!", player, "shoots", computer)
      else: # computer is bear, player is ninja
        print("You lose!", computer, "eats", player)
    elif computer == "Ninja":
      if player.lower() == "Cowboy":
        print("You lose!", computer, "defeats", player)
      else: # computer is ninja, player is bear
        print("You win!", player, "defeats", computer)

    print() #added for space between strings
    player = False
    computer = roles[randint(0,2)]
    play_again = input("Would you like to play again? (y/n) ")
    if play_again == 'y':
      player = False
      f = roles[randint(0,2)]
    else:
        print("Thanks for playing! ")
        break



