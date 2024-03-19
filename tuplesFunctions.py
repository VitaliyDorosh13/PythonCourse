# Tuple minimum 
# Create a tuple contains a set of numbers
lowest_value = (1,5 ,6, 7, 11, 22, 100, 33)

# Use the minimum funct to return the lowest value item in the tuple
print(min(lowest_value))

# Tuple maximum 
# Create a tuple contains a set of numbers 
highest_value  = (1, 2, 5, 11, 55, 88, 99, 22)

# Use the maximum function to return the highest value in th tuple
print(max(highest_value))

# Tuple length
# Create a tuple with some items
super_hair = ('Super Stache', 'Macho Beard', 'Gargantuan Goat-tee', 'Villians Toupee', 'Unfortunate Baldness')

# Print out the numbers of items in our tuple
print(len(super_hair))

# 4 Sorted tuples
# A list of Villians Locked Awat in the Villianous Vault of Bad Guys
villians = ('Naughty Man', 'Skid Mark', 'Mister Millenial', 'Jack Hammer', 'The Spelling Bee',
            'Drank All the Milk Man', 'Wonder Wedgie')

# Print out a sorted list of our villians tuple
print(sorted(villians))

# Sort tuple
# A tuple of number we are going to sort
numbers_sort = (10, 20, 30 ,313, 14, 22, 88, 55)

# Sort numbers in our tuple
print(sorted(numbers_sort))

# Summmirize a tuple
# A tuple of numbers we are going to sum
numbers_sum = (10, 20, 5, 2, 18)
# Summing items in a tuple
print(sum(numbers_sum))

# 5 Convert data from another structure
# A list we will onvert to a tuple
villianList = ['Naughty Man ', 'Skid Mark ', 'Mister Millenial ', 'JackHammer ', 'The Spelling Bee ', 
               'Drank All The Milk Man ', 'Wonder Wedgie ', 'Escape Goat']

# Using tuple() to convert villianList to a tuple
tuple(villianList)

# A string we will convert to a tuple
villian1 = "Musstang Head"
tuple(villian1)

print(villianList)
print(villian1)

# 6 Deleting whole tuple
# A tuple full of facial hair styles for villians and heroes
fecial_hair = ('Super Stache', 'macho Beard', 'Gargantuan Goat-tee', 'Face Mullet')

# Print out facial hair
print(fecial_hair)

# Using del to delete a tuple enterely
del fecial_hair

# Print out
print(fecial_hair)

