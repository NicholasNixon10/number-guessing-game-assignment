import random
randomNumber = random.randint(1,101)

guess = int(input("guess a number between 1-100: "))

while True:

    if guess > randomNumber:
        print("the number is smaller.")
        guess = int(input("guess again: "))   
    elif guess < randomNumber:
        print("the number is larger.")
        guess = int(input("guess again: "))
    if guess == randomNumber :
        print("you guessed the correct number!")
        break