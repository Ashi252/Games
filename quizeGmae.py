import time, datetime,pytz
print("Welcome to Fun Quiz!")
while True:
    score = 0
    dateT = datetime.datetime.now(tz=pytz.timezone('universal'))
    time.sleep(1)
    Option = input("Do you want to play and also know what time it is?\n ")
    if 'yes' in Option.lower():
        print(dateT)
    elif  'yes' not in Option.lower():
        quit()
    time.sleep(2)
    print("Cool! let's play")
    print("-----Hint: Answers are in Title case------- ")
    try:
        answer = input("Who is the CEO of Apple?\n")
        if "Elon Musk" in answer.title():
                print("correct")
                score +=1
        else:
            print("incorrect")
        time.sleep(2)
    except(ValueError):
                print("Invalid, please Enter words or Letters")
    try:
        answer = input("Who is the CEO of META?\n")
        if "Mack Zuckerberg" in answer.title():
                print("correct")
                score +=1
        else:
                print("incorrect")
        time.sleep(2)
    except(ValueError):
            print("Invalid, please Enter words or Letters")
    try:
        answer = input("Who is the CEO of Google?\n")
        if "Larry" in answer.title():
                print("correct")
                score +=1
        else:
                print("incorrect")
        time.sleep(2)
    except(ValueError):
                print("Invalid, please Enter words or Letters")
    try:
        answer = input("Is python a high level programming language?\n")
        if "Yes" in answer.title():
                print("correct")
                score +=1
        else:
                print("incorrect")
        time.sleep(2)
    except(ValueError):
                print("Invalid, please Enter words or Letters")
    try:
        answer = input("Who is the President of the United States?\n")
        if "Jeo Biden" in answer.title():
                print("correct")
                score +=2
        else:
                print("incorrect")
        time.sleep(2)
    except(ValueError):
                print("Invalid, please Enter words or Letters")
    try:
        answer = input("Who is the president of France?\n")
        if "Emmanuel Macron" in answer.title():
                print("correct")
                score +=2
        else:
                print("incorrect")
        time.sleep(2)
    except(ValueError):
                print("Invalid, please Enter words or Letters")
    try:
        answer = input("What statement is used to display the data stored in a table in SQL?\n")
        if "Select" in answer.title():
                print("correct")
                score +=3
        else:
                print("incorrect")
        time.sleep(2)
    except(ValueError):
                print("Invalid, please Enter words or Letters")
    try:
        answer = input("Who is the president of Nigeria?\n")
        if "Bola Ahmed Tinubu" in answer.title():
                print("correct")
                score +=2
        else:
                print("incorrect")
        time.sleep(2)
    except(ValueError):
            print("Invalid, please Enter words or Letters")

    print(" you got " + str(score/10*100) + "%")
    score= int(score)
    if score == 50:
            print("Good jod")
    elif score >50:
            print("Well done! you are Amazing.")
    else :
        print("you tried")


    rerun= input("Do you wish to play again?")
    if 'yes' in rerun:
        print("Okay! if you ready let go.")
    else:
        break
