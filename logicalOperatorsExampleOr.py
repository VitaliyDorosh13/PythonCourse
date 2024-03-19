#Variables to check
wonderBoyAllowance = 20
newCape = 20
newShoes = 50

#Check if you can afford a new cape OR if you can afford new shoes

if wonderBoyAllowance >= newCape or wonderBoyAllowance >= newShoes:
    print("Looks like you can either afford a new cape of new shoes")
    print("That's good, because one of them are really stinky!")

#If boxth the conditions fail, the else below triggers
#If even one of the conditions are true, the else does not trigger
    
else:
    print("That's a shame, because one of then is really stanky")