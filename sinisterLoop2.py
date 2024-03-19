# create a variable to hold Wonder Boy's password
password = ''
passwordAttempts = 0

print("Welcome to Optimal Dad's Vault of Gadgets!")

while password != "wonderboyiscool2023":
    print("Please enter your password to access some fun tech!")
    password = input()
    password = password.lower()
    passwordAttempts += passwordAttempts + 1

    if password == "wonderboyiscool2023":
        print("You entered the correct password!", password)
        print("Please take whatever gadgets you need!")
        print("Don't touch the Doom Canon though - that belongs to Optimal Dad!")
    elif passwordAttempts == 3:
        print("Sorry, you are out of attempts")
        break