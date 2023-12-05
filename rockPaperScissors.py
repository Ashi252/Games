import random

user_Score = 0
computer_score = 0
option = ['rock', 'paper', 'scissors']

while True:
    user = input("Type Rock or Paper or Scissors, else exit with 'q': ")
    if user == 'q':
        break
    if user not in option.lower():
        continue
    randNumber = random.randint(0, 2)
    computerGuess = option[randNumber]
    if user.lower() == "rock" and computerGuess =="scissors":
        print("You won!")
        user_Score +=1
    elif user.lower() == "paper" and computerGuess =="rock":
        print("You won!")
        user_Score +=1
    elif user.lower() == "scissors" and computerGuess =="paper":
        print("You won!")
        user_Score +=1
    else:
        print("you lost")
        computer_score +=1
    print("Computer picked", computerGuess +".")
print("you won", user_Score, "times.")
print("The computer won", computer_score, "times.")
print("GOODBYE!")

