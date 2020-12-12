from random import randint

#create a list of choices
choices = ["Rock", "Paper", "Scissors"]

#assign a random choice to the computer
computer = choices[randint(0,2)]

#set user to False
user = False

while user == False:
#set user to True
    user = input("Rock, Paper, Scissors? ")
    if user == computer:
        print("Tie!")
    elif user == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", user)
        else:
            print("You win!", user, "smashes", computer)
    elif user == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", user)
        else:
            print("You win!", user, "covers", computer)
    elif user == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", user)
        else:
            print("You win!", user, "cut", computer)
    else:
        print("That's not a valid Choice. Please Check your spelling!")
    #user was initially set to True, but we want it to be False so that way the loop can still continue
    user = False
    computer = choices[randint(0,2)]