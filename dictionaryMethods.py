# Create a dictionary name algebro and fill it with key-value pairs
algebro = {'codename':'Algebro', 'power':'Mathemagic', 'real-name':'Al.G.Bro'}

# Print just the keys in the algebro dictionary
print(algebro.keys())

# Print just the values in the algebro dictionary
print(algebro.values())

# Print the key-value pairs
print(algebro.items())

# Using a for loop to iterate through and print out dictionary
for key, value in algebro.items():
    print('The key is: ', key, ' and the values is: ', value)