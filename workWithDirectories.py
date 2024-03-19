# Import the modeule os
# This is used to work with operating system info
import os

# Use the getcwd() method of the os module
# To see what directory we are in
os.getcwd()

# Create a new directory or folder 
# os.mkdir("newDirectory")

# Using the chdir() method to change directories
os.chdir("d:/py directory/newDirectory")
print(os.getcwd())

# Switch back to the original directory
# Remember to use own directory
os.chdir("d:/py directory")

# Verify that we are back to the original directory
print("Back ti the original directory")
print(os.getcwd())

# Deleting the newDirectory directory
# Using the rmdir() method
os.rmdir('newDirectory')