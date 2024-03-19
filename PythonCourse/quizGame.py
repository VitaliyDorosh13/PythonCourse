print("Welcom to my game")

playing = input("Do you wanna play? ")
print(playing)

if playing.lower() != "yes":
    quit()

print("Okay! Lets play")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "checking processor unit":
    print("Correct!")
    score+=1
else:
    print("Incorect")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct")
    score+=1
else:
    print("Incorrect")


answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct")
    score+=1
else:
    print("Incorrect")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct")
else:
    print("Incorrect")

print("You got " + str(score) + " question correct")
print("You got " + str((score/4)*100) + " %.")
