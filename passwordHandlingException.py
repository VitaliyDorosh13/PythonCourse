# Example of exception handling a ValueError
repeat = 1
while repeat > 0:
    try:
        pin = int(input("Enter your pin number:"))
        print("You entered: ", pin)
        repeat = 0
    except ValueError:
        print("You must only enter a numeric value")
        repeat = 1