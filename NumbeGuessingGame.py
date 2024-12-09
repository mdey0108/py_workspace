import random

def number_guessing_game():
    number_to_guess = random.randint(1, 20)
    number_of_tries = 0
    has_guessed_correctly = False

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 20.")
    print("You have 5 attempts to guess it.")

    while number_of_tries < 5 and not has_guessed_correctly:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        number_of_tries += 1

        if guess < number_to_guess:
            print("Your guess is too low. Try again.")
        elif guess > number_to_guess:
            print("Your guess is too high. Try again.")
        else:
            has_guessed_correctly = True
            print(f"Congratulations! You've guessed the number in {number_of_tries} tries.")

    if not has_guessed_correctly:
        print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")

    # Calculate and display score
    score = (100 if has_guessed_correctly else 0) - (number_of_tries * 20)
    score = max(score, 0)  # Ensure the score is not negative
    print(f"Your score: {score}%")

# Run the game
number_guessing_game()
