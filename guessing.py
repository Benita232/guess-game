import random
import time


def guess_number():
    # Randomly select a number between 1 and 100 for the player to guess
    number_to_guess = random.randint(1, 100)
    max_attempts = 7  # Define maximum number of guesses allowed
    attempt = 0  # Initialize the attempt counter

    # Print introductory messages with pauses for better user experience
    print("----------------Welcome to the Number Guessing Game!----------------------")
    time.sleep(2)
    print("I have selected a number between 1 and 100. Can you guess it?")
    time.sleep(2)
    print(f"You only have {max_attempts} attempts.")
    time.sleep(2)

    # Record the start time of the game to track elapsed time
    start_time = time.time()

    # Main game loop: repeat until the player runs out of attempts or guesses right
    while attempt < max_attempts:
        
        print(f"Attempt {attempt + 1} of {max_attempts}")
        user_input = input("Enter your guess or type 'i give up' to quit: ").strip().lower()

        # Allow the player to quit early
        if user_input == 'i give up':
            time.sleep(1)
            print(f"You gave up! The number was {number_to_guess}.")
            break

        # Validate input is a number
        try:
            guess = int(user_input)
        except ValueError:
            time.sleep(1)
            print("Invalid input. Please enter a number between 1 and 100 or 'i give up'.")
            time.sleep(2)
            continue  # Ask again without counting this as an attempt

        # Check if guess is within valid range
        if guess < 1 or guess > 100:
            time.sleep(1)
            print("Please guess a number between 1 and 100.")
            time.sleep(2)
            continue

        attempt += 1  # Increment attempt count after a valid guess

        # Check guess against the hidden number and provide feedback
        if guess == number_to_guess:
            end_time = time.time()  # Record end time on correct guess
            elapsed = end_time - start_time  # Calculate total time taken
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempt} attempts.")
            print(f"Time taken: {elapsed:.2f} seconds")
            break
        elif guess < number_to_guess:
            time.sleep(1)
            print("Too low! Try again.")
            time.sleep(2)
        else:
            time.sleep(1)
            print("Too high! Try again.")
            time.sleep(2)
    else:
        # Executed if loop ends without a break (player used all attempts)
        end_time = time.time()
        elapsed = end_time - start_time
        print(f"Sorry, you've used all your {max_attempts} attempts. The number was {number_to_guess}.")
        print(f"Time taken: {elapsed:.2f} seconds")

if __name__ == "__main__":
    guess_number()