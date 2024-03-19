# 7 Count() method of tuple
# Tuple contains all of the letters used to spell Missisisppi
state = ('M', 'i', 's', 's', 'i', 's', 'i', 's', 'i', 'p', 'p', 'i')

# Note: You could, technically, also easily create the tuple using state = tuple('Missisisippi')
# with the tuple() command, which automatically converts a string into a tuple.
# Count the number of times "i" appears in our tuple and print out the result
print("There are this many of the letter i in Missisisippi: ")
print(state.count('i'))

# Count the number of times 's' appears in Missisisippi
print("There are this many of letters 's' in Missisisippi")
print(state.count('s'))

# 8 
# Tuple containing all of the letters used to spell Missisisippi
state = ('M', "i", "s", "s", "i", "s", "i", "s", "i", "p", "p", "i")
# Checking to see if "z" or "i" appears in our state tuple
print('z' in state)
print('i' in state)