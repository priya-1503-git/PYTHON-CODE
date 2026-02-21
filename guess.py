import random
number=random.randint(1,100)
attempts=0
print("--NUMBER GUESSING GAME")
print("--GUESS NUMBER B/W 1 TO 100")

while True:
    guess =int(input("ENTER A GUESS:"))
    attempts+=1

    if guess<number:
        print("TOO LOW,TRY AGAIN")
    elif guess>number:
        print("HIGH,TRY AGAIN")
    else:
        print("CONGRALUATIONS-----")
        print("YOU GUESSED THE NUMBER IN",attempts,"attempts")
        break