# Import the random module so we can randomly generate numbers 
import random
import time

# Create a Superhero class that will act as a template for any heroes we create
class Superhero():

    # Initialize our class and setting its attributes
    def __init__(self):
        self.superName = superName
        self.power = power
        self.braun = braun
        self.brains = brains
        self.stamina = stamina
        self.wisdom = wisdom
        self.constitution = constitution
        self.dexterity = dexterity
        self.speed = speed

# Adding random values to each stat the random() module 
braun = random.randint(1, 20)
brains = random.randint(1, 20)
stamina = random.randint(1, 20)
wisdom = random.randint(1, 20)
constitution = random.randint(1, 20)
dexterity = random.randint(1, 20)
speed = random.randint(1, 20)

print("Please enter your super hero name: ")

# Creating a list of possible super powers
superPowers = ['Flying', 'Super Strength', 'Telepathy', 'Super Speed', 'Can a Eat a Lot of Hot Dogs', 
               'Good At Skipping Rope']

# Randomly choosing a super power from the superPowerList and assigning it to the varable
power = random.choice(superPowers)

# Creating lists of possible first and last name
superFirstName = ["wonder", 'Whatta', "Rapid", 'Incrediable', 'Astonishing', 'Decent', 'Stupendous', 'Yhat Guy']
superLastName = ['Boy', 'Man', 'Dingo', 'Beefcake', ' Girl', 'Woman', 'Guy', 'Hero', 'Max', 'Dream']

# Randomizing Super HEro Name
# We do this by choosing one name from each of our two name lists
# And adding it to the variable superName
superName = random.choice(superFirstName) + " " + random.choice(superLastName)

# Creating a subclass of superhero named Mutate
# Mutate heroes will get a +10 bonus to thir speed score
class Mutate(Superhero):
    def __init__(self):
        Superhero.__init__(self)
        print("You created a Mutate!")
        self.speed = self.speed + 10
        self.superName = random.choice(superFirstName) + " " + random.choice(superLastName)

# Creating a subcass of Superhero Robot
# Robot heroes will get a +10 bonus to their braun score
class Robot(Superhero):
    def init__(self):
        Superhero.__init__(self)
        print("You created a robot")
        self.braun = self.braun + 10
        self.superName = random.choice(superFirstName) + " " + random.choice(superLastName)

# Introductory text
print("Are you ready to create a super hero with the Super Hero Generator 3000?")

# Ask the user a question and prompt them for an answer
# input() 'listens' to what they type on their keyboard
# We then use upper() to change the users answer to all uppercase letters
print("Enter Y/N:")

answer = input()
answer = answer.upper()

# While loop to check for the answer "Y"
# This loop will continue while the value of answer IS NOT "Y"
# Only when the user types "Y" will the loop exit and the program continue
while answer != "Y":
    print("I'm sorry, but you have to choose Y to continue!")

print("Choose Y/N:")
answer = input()
answer = (answer.upper())
print("Great, let's get started!")

# Letting the user choose which type of hero to create
print("Choose from the following hero options: ")
print("Press 1 for a Regular Superhero")
print("Press 2 for a Mutate Superhero")
print("Press 3 for a Robot Superhero")

answer2 = input()
if answer2 == '1':
    # Creating the Superhero object
    hero = Superhero()
    
    # We print out the result of the created object, including it's parameters
    print("You created a regular super hero!")
    print("Generating stats, name, and super powers")

    # Creating dramatic effect
    for i in range(1):
        print("......")
        time.sleep(2)
        print("nah .. you won't like THAT one .. ")
    for i in range(2):
        print(".......")
        time.sleep(2)
    print("(almost there....)")
    print(" ")

    # We print out the results of the created object, including its parameters
    print("Your name is %s." % (hero.superName))
    print("Your new stats are: ", hero.power)
    print(" ")

    print("Brains: ", hero.brains)
    print("Braun: ", hero.braun)
    print("Stamina: ", hero.stamina)
    print("Wisdom: ", hero.wisdom)
    print("Constitution: ", hero.constitution)
    print("Dexterity: ", hero.dexterity)
    print("Speed", hero.speed)
    print(" ")

elif answer2 == '2':
    
    # Creating a Mutate object
    hero2 = Mutate()
    print("Generating stats, name, and super powers")

    # Creating dramatic effect
    for i in range(1):
        print("........")
        time.sleep(2)
        print("nah ... you wouldn't like THAT one ... ")
    for i in range(2):
        print("........")
        time.sleep(2)

    print("Your name is %s." % (hero2.superName))
    print("Your super power is: ", hero2.power)
    print("Your new stats are:")
    print("")
    print("Brains: ", hero2.brains)
    print("Braun: ", hero2.braun)
    print("Stamina: ", hero2.stamina)
    print("Wisdom: ", hero2.wisdom)
    print("Constitution: ", hero2.constitution)
    print("Dexterity: ", hero2.dexterity)
    print("Speed ", hero2.speed)
    print("")

elif answer2 == '3':

    # Create a Robot character
    hero3 = Robot()
    print("Generating stats, name, and super powers")

    # Creating dramatic effect
    for i in range(1):
        print("........")
        time.sleep(2)
        print("nah ... you wouldn't like THAT one ... ")
    for i in range(2):
        print("........")
        time.sleep(2)

    print("Your name is %s." % (hero3.superName))
    print("Your super power is: ", hero3.power)
    print("Your new stats are:")
    print("")
    print("Brains: ", hero3.brains)
    print("Braun: ", hero3.braun)
    print("Stamina: ", hero3.stamina)
    print("Wisdom: ", hero3.wisdom)
    print("Constitution: ", hero3.constitution)
    print("Dexterity: ", hero3.dexterity)
    print("Speed ", hero3.speed)
    print("")

else:
    print("You didn't choose the proper answer! Program will now self-destruct")

