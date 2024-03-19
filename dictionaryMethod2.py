#1
# Create a dictionary name algebro and fill it with key-value pairs
algebro = {'codename':'Algebro', 'power':'Mathemagic', 'real-name':'Al.G.Bro'}

# Add the key 'age' to the dictionary 'algebro' and assign it the value '42'
algebro['age'] = 42

# Print out algebro to show the newly added result
print(algebro)

#2
# Updating a value for our 'age' key
algebro['age'] = 43

# Printing the algebro dictionary to see the updated value of the  'age' key
print(algebro)

#3
# Create a dictionary name algebro and fill it with key-value pairs
algebro = {'codename': 'Algebro', 'power': 'Mathemagics', 'real-name':'Al. G. Bro.'}

# Using dict.update() to add a key-pair value to our 'algebro' dictionary
# Note the use of curly braces {}, mixed with parentheses ()
algebro.update({'villainType': 'mutate'})

# Printing out the results
print(algebro)

#4
# USing the del keyword to delete a key-value pair
del algebro['power']

# Printing algebro to verify that we properly removed the key-value pair
print(algebro)

#5
# Create a dictionary name algebro and fill it with key-value pairs
algebro = {'codename': 'Algebro', 'power': 'Mathemagics', 'real-name': 'Al.G. Bro.'}
algebro.clear()
print(algebro)

#6
# Deleting the algebro dictionary using the del keyword
del algebro
# Printing the deleted algebro, which results in an error
# This occurs because algebro no longer exists
print(algebro)

'''
Here’s a list of these other dictionary methods: go forth and experiment wildly!
• dict.clear( ): Removes all of the items in a dictionary
• dict.copy( ): Returns a copy of a dictionary
• dict.fromkeys( ): Used to create a dictionary from a sequence
• dict.get( ): Returns the value of a specified key
• dict.items( ): Returns a view of the given dictionary’s key/pair values
• dict.keys( ): Returns the keys in a dictionary as a view
• dict.popitem( ): Returns – and also removes – a dictionary element
• dict.pop( ): Returns – and removes – an element from a specified key
• dict.setdefault( ): Checks to see if a key is present and, if not, insets
the key (with a value)
• dict.values( ): Returns all of the values in a dictionary as a view
• dict.update( ): Used to update a dictionary
Other methods you can use on a dictionary include
• any( ): Tests whether an element of an iterable is True
• all( ): If all elements of an iterable are True, this returns True
• dict( ): Used to create a dictionary
• enumerate( ): Creates or returns an enumerate object
• iter( ): Returns an iterator for a given object
• len( ): Returns the length of an object
• max( ): Returns the largest element
• min( ): Returns the smallest element
• sorted( ): Returns a sorted list
• sum( ): Sums all items
'''