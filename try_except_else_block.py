# Example of exception handling a ValueError
# Using a Try Except Else Block
# Enclose in a while loop
repeat = 1
while repeat > 0:
    try:
        pin = int(input("Enter your pin number: "))
    except ValueError:
        print("You must only enter a numeric value")
        repeat = 1
    else:
        print("You entered: ", pin)
        repeat = 0