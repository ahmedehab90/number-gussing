from numpy import random

def defMode(mode, counter):
    match mode:
        case "easy":
            x = random.randint(25)
        case "medium":
            x = random.randint(50)
        case "hard":
            x = random.randint(100)
    chances(x, counter, mode)

def chances(x, counter, mode):
    if counter == 0 :
        print("You lost")
        print("the number was "+ str(x))
        return 0
    else :
        match mode:
            case "easy":
                guessing = int(input("Enter a number between 0 and 25: "))
            case "medium":
                guessing = int(input("Enter a number between 0 and 50: "))
            case "hard":
                guessing = int(input("Enter a number between 0 and 100: "))
        game(x, guessing, counter, mode)

def game(x, guessing, counter, mode):
    if guessing == x :
        print("Well done!")
        print("You won!")
    elif guessing > x :
        print("Your guessing is high")
        counter = counter - 1
        print("You have "+ str(counter) + " chances left")
        chances(x, counter, mode)
    else :
        print("Your guessing is low")
        counter = counter - 1
        print("You have "+ str(counter) +" chances left")
        chances(x, counter, mode)

difficulty = input("Enter the difficulty mode (easy/ medium/ hard): ")
if difficulty == "easy" :
    print("you have 3 chances")
    defMode(difficulty, 3)
elif difficulty == "medium":
    defMode(difficulty, 5)
else :
    defMode(difficulty, 10)