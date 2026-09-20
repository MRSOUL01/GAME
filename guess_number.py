import random as rn

guess =  rn.randint(1, 100)

print("Welcome to the Guess the Number Game!")
print("I'm thinking of a number between 1 and 100.")
print("Can you guess what it is?")

user_guess = int(input("Enter your guess: "))

if user_guess == guess:
    print(f"Congratulations! You guessed the number{guess}!")
elif user_guess != 0:
    print("No worries, i will give you a hint!, start guessing again")

    guess_rn2 = 0
    while guess_rn2 != guess:
    
        guess_rn2 = int(input("Enter your guess: "))

        if guess == guess_rn2:
            print("Correct! You win!")
            break
        elif guess_rn2 < guess:
            print("Too low. Try again.")
        elif guess_rn2 > guess:
            print("Too high. Try again.")