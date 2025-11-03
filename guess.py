import random

tries = 3 
number = random.randint(1,10)
finded = False

while tries > 0:
    guess = input("Guess the number. Number: ")
    if guess == number :
        print("You find them YEAHHHHHHHH!!!!!!!")
        finded = True
        break
    elif guess == "":
        print("Type a number")
    else:
        print("You failed try again")
        tries-=1

if finded:
   pass
else:
    print("GAME OVER")
