# Create our variables representing our allowance and the cost of a new cape

wonderBoyAlloance = 20
newCape = 20
print("The new cape sure is shiny. I wonder if you can afford it..")

if wonderBoyAlloance > newCape:
    print("Congrats! You have enough to buy that new cape!")
    print("And it looks like you have some money left over.")
    print("How about getting a hair cut? You hair is covering your mask!")
# Check to see if allowance is the same exact price as the new cape
elif wonderBoyAlloance == newCape:
    print("You have exactly enough money to purchase the cape!")
    print("No change for you!")
    print("Eh...and no tip for me I see...")
elif wonderBoyAlloance == 0:
    print("Oh boy, you are broke!")
    print("Maybe it's time to hang up the cape and grab an apron!")
    print("Time to become...Bag Boy!")
# If all other conditions fail, this else will trigger
else:
    print("Looks like you'll have to keep wearing that towel as a cape...")
    print("Maybe if you ask nicely Wonder Dad will give you a raise...")