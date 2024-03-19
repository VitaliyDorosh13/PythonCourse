# Import random module to use for randomizing numbers and settingd later
import random

# Import the time module to crete a delay
import time

brains = 0
braun = 0
stamina = 0
wisdom = 0
power = 0
constitution = 0
dexterity = 0
speed = 0
answer = ' '

# Creating a list of possible super powers
superPowers = ['Flying', 'Super Strength', 'Telepathy', 'Super Speed', 'Can Eat a Lot ofHot Dogs', 'Good At Skipping Rope']

# Creaying lists of possible first and last name 
superFirstName = ['Wonder', 'Whatta', 'Rapid', 'Incredible', 'Astonish', 'Decent', 'Stuendous', 'Above-avarage',
                  'That Guy', 'Inprobably']
superLastName = ['Boy', 'Man', 'Dingo', 'Beefcake', 'Girl', 'Woman', 'Guy', 'Hero', 'Max', 'Dream', 'Macho Man',
                 'Stallion']

# Introductory text
print("Are you ready to create a super hero with the Super Hero Generator 3000?")

# Ask the user a question and prompt them for an answer
# input() 'listens' to what they type on their keyboard
# We then use upper() to change users answer to all uppercase letters
print("Enter Y/N? ")

answer = input()
answer = answer.upper()

# While loop to check for the answer "Y"
# This loop will continue while the value of answer IS NOT "Y"
# Only when the user types 'Y' the loop exit and the programm continue

while answer != "Y":
    print("I'm sorry, but you have to choose Y to continue!")
    print("Choose Y/N")
    answer = input()
    answer = answer.upper()
print("Great, let's get started")

print("Randomizing name..")

# Creating suspense using the time() function
for i  in range(3):
    print(".......")
    time.sleep(2)

print("I bet you can't stand the suspense")
print(" ")

# Randomize Super EHro Name 
# We do this by choosing one name from each of our two name lists
# And adding it to the variable superName

superName = random.choice(superFirstName) + " " + random.choice(superLastName)

print("You Super Hero Name is:")
print(superName)

print("")
print("Now it's time to see what super power you have!)")
print("(generating super hero power...)")

# Creating dramatic effect again
for i in range(2):
    print("......")
    time.sleep(3)
print(" (nah.. you would't like That one..)")

for i in range(2):
    print("......")
    time.sleep(2)
print(" (almost there...) ")

# Randomly choosing a super power from the superPower list and assigning it to the variable power
power = random.choice(superPowers)

# Printing out the variables power and some text
print("You new power is: ")
print(power)
print(" ")

print("Last but not least, let's generate your ststs")
print("Will you be super smart? Super strong? Super Good Looking?")
print("Time to find out")

# Creating dramatic effect and slowing the program down again
for i in range(3):
    print("......")
    time.sleep(2)

# Randomly filling each of the below variables with a new value
# The new values will range from 1-20

brains = random.randint(1, 20)
braun = random.randint(1, 20)
stamina = random.randint(1, 20)
wisdom = random.randint(1, 20)
constitution = random.randint(1, 20)
dexterity = random.randint(1, 20)
speed = random.randint(1, 20)

# Printing out the statistics

print("You new state are:")
print(" ")

print("Brains: ", brains)
print("Braun: ", braun)
print("Stamina: ", stamina)
print("Wisdom: ", wisdom)
print("Constitution: ", constitution)
print("Dexterity: ", dexterity)
print("Speed: ", speed)
print("")

# Printing out a full summary of the generated super hero
# This includes the hero's name, super power, and stats
print("Here is a summary of your new Super Hero!")
print("Thanks for using the Super Hero Generator 3000!")
print("Tell all your friends!")
print("")
print("Character Summary:")
print("")
print("")
print("Super Hero Name: ", superName)
print("Super Power: ", power)
print("")
print("Brains: ", brains)
print("Braun: ", braun)
print("Stamina: ", stamina)
print("Wisdom: ", wisdom)
print("Constitution: ", constitution)
print("Dexterity: ", dexterity)
print("Speed: ", speed)