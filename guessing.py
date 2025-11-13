import random

def guess_number():
    attempt = 0
    number_to_guess = random.randint(1, 100)
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")
    print("You only have 5 attempts.: ")
    
    while True:
        if attempt == 5:
            try:
                guess = int(input("Enter your guess (or type 'i give up' to quit): "))
                attempt += 1
                if guess < 1 or guess > 100:
                    print("Please guess a number between 1 and 100.")
                    continue
                if guess < number_to_guess:
                    print("Too low! Try again.")
                elif guess > number_to_guess:
                    print("Too high! Try again.")
                else:
                    print(f"Congratulations! You've guessed the number {number_to_guess} in {attempt} attempts.")
                    break
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 100 ")
        else:    
            print(f" your attempt is {attempt}. Enter 'i give up' to reveal the number or try again.")
       
            break
        
    
    
if __name__ == "__main__":
    guess_number()