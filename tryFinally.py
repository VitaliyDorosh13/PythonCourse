# Example of exception handling a ValueError
# Using a Try Except Else Finally block

try:
    pin = int(input("Enter your pin number: "))
except ValueError:
    print("You must only enter a numeric value")
else:
    print("You entered: ", pin)
finally:
    print("Are we done yet?")