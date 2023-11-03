import random

number = random.randint(1, 10)
print("I'm thinking of a number between 1 and 10, can you guess it?")
print("You have 5 guesses to guess the number.")
print("_____________________________________________________________")


def guess_number():
    user_input = int(input("Enter a number between 1 and 10: "))
    guesses=0
    try:
        while guesses <= 5:
            if user_input == number:
                print("You guessed it right!")
                break
            elif guesses == 5:
                print("No guesses left! Game over!")
                break
            elif user_input > number:
                print("Your guess is too high.")
                guesses += 1
                print("You have", 5-guesses, "guesses left.")
                user_input = int(input("Enter a number between 1 and 10: "))
            elif user_input < number:
                print("Your guess is too low.")
                guesses += 1
                print("You have", 5-guesses, "guesses left.")
                user_input = int(input("Enter a number between 1 and 10: "))
            elif user_input > 10 or user_input < 1:
                print("You did not enter a number between 1 and 10.")
                guess_number()
            # if the 5 guesses have been used print game over
            
            
    except ValueError:
        print("You did not enter an integer.")
        guess_number()

guess_number()