import random

def get_random_number(start: int = 1, end: int = 100) -> int:
    """Generate a random number between start and end (inclusive)."""
    return random.randint(start, end)

def get_user_guess() -> int:
    """Prompt the user for a guess and validate input."""
    while True:
        try:
            return int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_game(start: int = 1, end: int = 100) -> None:
    """Play the number guessing game."""
    print(f"🎯 Guess the number between {start} and {end}")
    target = get_random_number(start, end)
    attempts = 0

    while True:
        guess = get_user_guess()
        attempts += 1

        if guess < target:
            print("Too low! 📉")
        elif guess > target:
            print("Too high! 📈")
        else:
            print(f"✅ Correct! You guessed it in {attempts} tries.")
            break

if __name__ == "__main__":
    play_game()
