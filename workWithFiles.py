# This code is used to open a file
# However, since the file does not already exist
# Python instead creates it for us

newFile = open("CreatedFile.txt", 'w')

# This code os simillar to a print() statment
# However, instead of writing text or output to a user's computer screen
# It writes it to a file instead

newFile.write("Look, we created a brand new file using Python code")

# The close() function closes the file we are working on and saves it
# It's important to always close a file when we are finished with it
# to ensure we don't make any additions or mess up the file in anyway

newFile.close()