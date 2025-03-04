import random

answerInt = random.randint(1, 10)
guessInt = int(input("Guess a number between 1 and 10: "))

for i in range(10):
    if (guessInt == answerInt):
        print((str(answerInt)) + " is correct!")
        break
    else:
        guessInt = int(input("Try again: "))
        if (answerInt > guessInt):
            print("The answer is higher")
        else:
            print("The answer is lower")


print("Attempts used: " + str(i + 1))