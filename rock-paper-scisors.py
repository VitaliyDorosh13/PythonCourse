import random

#insertation variebles for checking win grade
user_wins = 0
comp_win = 0

#list with actions which comp or we can choose
options = ["rock", "paper", "scisors"]

#create a loop where will be work till someone win or lose
while True:

    #insert key word for the enter the game and choose action
    user_input = input("Type Rock/Scisors?Paper or Q to Quit").lower()
    if user_input == "q":
        quit()
        break
    
    #if-else statment where we choose action 
    if user_input in options:
        continue

    random_number = random.randint(0, 2)
    #rock: 0, paper: 1, scisors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scisors":
        print("You won")
        user_wins +=1
    
    elif user_input == "paper" and computer_pick == "rock":
        print("You win")
        user_wins +=1

    elif user_input == "scisors" and computer_pick == "scisors":
        print("You win")
        user_wins +=1

    else: 
        print("You lost")
        comp_win +=1
    print("You won ", user_wins, " times")
    print("The computer won, " comp_win, " times")
    print("Goodby")


