import random,time
while True:
    answer = input('Hi, do want to play: ')
    if 'yes' in answer.lower():
        print("Cool! let play")
    elif 'no' in  answer.lower():
        print("Okay Bye!")
        break
    else:
        print("Please enter yes or no thanks.")
        continue

    range = input("Type a number greater than 0: ").strip()
    if range.isdigit():
        range = int(range)
        if range <=0:
            print("please enter a number greater than 0, GOODBYE")
            quit()
    else:
        print("Please enter a number next time, GOODBYE!")
        quit()
    random_Guess = random.randint(0, range)
    guessCount = 0
    while True:
        guessCount += 1
        userGuess = input("Please make a guess: ").strip()
        if userGuess.isdigit():
            userGuess = int(userGuess)
        else:
            print("Please enter a number next time!")
            continue
        if userGuess == random_Guess:
            print("Good job! you got it right.")
            break
        elif userGuess >random_Guess:
            print("you were above the number")
        else:
            print("you are below the number")
    print("You got it in", guessCount,"guesses")
    time.sleep(5)