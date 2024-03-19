# Open the file CreatedFile.txt
read_me_seymore = open("CreatedFile.txt", 'r')

# Read the contents of he file
print(read_me_seymore.read())
read_me_seymore.close()

# This code is used to open a file
# However, since the file does not already exist
# Python instead creates it for us
# Remember, if the file name already exist, it will iwerwrite the existing one, erasing contests in the process

newFile = open("CreatedFile.txt", 'w')

# This code is simillar to a print() statment
# however, isntead of writing text or output to a user's computer screen
# It writes it to a fole instead

newFile.write("Look, we created a brand new file using Python code \n")
newFile.write("Here is a second line of text \n")

# The close() funct closes the file we are working on and saves it
# It is important to always close a file when we are finished it
# To ensure we don'r make any additions or mess up the file in anyway

newFile.close()

# Open the file CreatedFile.txt
read_me_seymore = open("CreatedFile.txt", 'r')

# Read the contens of the file
print(read_me_seymore.readline())

# Read he second line in the txt file
print(read_me_seymore.readline())

# Close the file again
read_me_seymore.close()