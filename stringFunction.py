#1
# Create a string of all uppercase letters
testString = "I AM YELLING"
print("Is the user yelling?")

# Check to see if the value of testString consist of all uppercase letters
print(testString.isupper())

# Create a string of all uppercase letters
testString = "I AM YELLING!"
print("Is the user yelling?")

#2
# Check to see if the value of testString consists of all uppercase letters
print(testString.islower())

# Create a string to check if the variable only consist letters
firstName = 'James4'

# Check to see if the value of firstName consist any numbers
print("Does you name contains any letters?")

if firstName.isalpha() == False:
    print("What are you, a robot?")

#3
# Create a string to check if the variable only contains numbers
userIQ = "2000"

# Check to see if the value if userIQ contains only numbers and no letters
if userIQ.isnumeric() == False:
    print("Numbers only please!")
else:
    print("Congrats, you know the difference between a number and a letter!")


#4
# Check to see if the value of UserIQ contains all spaces or whitespace characters
if userIQ.isspace() == True:
    print("Please enter a value other than a bunch of spaces you boob!")

#5
# Create a variable to count the number of characters it holds using len()
testPassword = "MyPasswordIsPassword"

print(len(testPassword))