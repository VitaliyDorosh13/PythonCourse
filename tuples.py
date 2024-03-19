#1
# Defining our tuple
villians = ('Eyebrow Raiser', 'Angry Heckler', 'Not So Happy Man', 'The Heck Raiser')

# Printing the items in a tuple
print(villians)

# Printing simple items in a tuple
print(villians[0])
print(villians[1])
print(villians[2])
print(villians[3])

# Ways to append tuple items to sentences
print("The first villian in the sinister", villians[0])
print("The second villian in the terrifying", villians[0])

print(villians[0:3])
print(villians[1:4])

#2
# Creating a tuple of my purple capes
purpleCapes = ('Purple Frillay Cape', 'Purple Short cape', 'Purple cape with Holes In it')

# Creating a tuple of my Polka Dot capes
polkaCapes = ('Black and White Polka Dot Cape', 'White and Beige Polka Dot Cape', 
              'Blue Polka Dot Cape Missing the Blue Polka Dots')

# Concetination - or adding - my two tuples of capes together into a new tuple
allMyCapes = (purpleCapes + polkaCapes)

# Printing out the values of the newly created tuple
print(allMyCapes)
print((allMyCapes[1] + " ") * 3)