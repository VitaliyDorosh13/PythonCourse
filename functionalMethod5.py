animals = ["ferret", "vole", "gecko"]

# Sort list using 'key' - spesial parameter to sotring
print(sorted(animals, key=len))

# Method that reverse list
def reverse_len(s):
    return -len(s)

# the output of reverse list
print(sorted(animals, key=reverse_len))
