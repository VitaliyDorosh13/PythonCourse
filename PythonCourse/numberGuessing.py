import random


#number guessing game

top_of_range = input("Type a number ")

#checking input number from keyboard
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger then 0 next time")
        quit()
else:
    print("Please type a number larger then 0 next time")
    quit()

#insert the value from keyboard using import method random* 
random_number=random.randint(0,top_of_range)


guesses = 0

#generate cycle where will be work till guesses number will equal random
while True:

    #
    guesses += 1 
    user_guess = input("Make a guess ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue

#using if-elif statment
    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You're below the number")
    else:
        print("You're under the number")
print("You got it " + guesses)


