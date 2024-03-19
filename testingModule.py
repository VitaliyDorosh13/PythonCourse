# We first have to import our module
# We import our module by using the name of the file, minus the .py extension

import ourFirstModule

# Now we call the function to use it
ourFirstModule.firstFunction()

# Calling our seconf function
ourFirstModule.secondFunction()

# Calling and printing a variable withing our module

print("The value of a is:", ourFirstModule.a)

# Print the helpfile for firstFunction()
help(ourFirstModule)