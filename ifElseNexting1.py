# Variables to check
wonderBotAloowance = 20
newCape = 20
newShoes = 50

# Checks if you can afford a new cape

if wonderBotAloowance >= newCape:
    print("You can afford a new cape")
    print("But how about new shoes?")

# When the if check to see if you can afford the new cape passes it does this
    if wonderBotAloowance >= newShoes:
        print("Look like you can afford new shoes as well")
        print("That's good, because the old ones are really stinky")
        print("But you can afford both together?")

# If you can afford the shoes, but can afford the cape, it does this 
    else:
            print("You can only afford the new cape, sorry")
# If both the conditions fail, the else below triggers
# If even one of the conditionals are true, this else does not trigger
else:
     print("That's a shame, because one of them is relly stanky")