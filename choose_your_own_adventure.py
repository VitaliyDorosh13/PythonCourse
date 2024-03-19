name = input("type your name: ")
print("Welcome", name, "to this adventure")

answer = input("You are on a dirt road, ou can turn left ot right. Choose your way").lower()

if answer == "left":
    answer = input("You come to river, ou can walk around or swim: ")
    if answer == "swim":
        print("You swam accross and were eaten by an aligator")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game")   
    else:
        print("Not a valid option. You lose")
elif answer == "right":
    answer = input("You can to a bridge, it looks wobbly, do you want to cross it or head back(cross/back)? ")

    if answer == "back":
        print("You go back and lose")
    elif answer == "cross":
        answer == input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")
        if answer == "yes":
            print("You talk to the stranger and they give you gold. You win")
        elif answer == "no":
            print("You ignore the stranger and they are offended and lose")
        else:
            print("Not a valid option. You lose")

else:
    print("Not a valid option. You lose")

    print("Thanks for you trying", name)
