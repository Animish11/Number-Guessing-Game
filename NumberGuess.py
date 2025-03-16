import random
import time

# Global dictionary to track high scores for each difficulty
high_scores = {'Easy': None, 'Medium': None, 'Hard': None}

def get_valid_guess():
    """Prompt the user for a valid guess between 1 and 100."""
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def provide_hint(number, hint_level):
    """Provide different hints based on the hint level."""
    if hint_level == 0:
        return "Hint: The number is even." if number % 2 == 0 else "Hint: The number is odd."
    elif hint_level == 1:
        return "Hint: The number is a multiple of 5." if number % 5 == 0 else "Hint: The number is not a multiple of 5."
    elif hint_level == 2:
        lower_bound = ((number - 1) // 20) * 20 + 1
        upper_bound = lower_bound + 19
        return f"Hint: The number is between {lower_bound} and {upper_bound}."
    return ""

def play_game():
    """Main game logic for a single round."""
    print("\nWelcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.\n")

    # Difficulty selection
    difficulty_choice = input(
        "Choose difficulty:\n"
        "1. Easy (10 chances)\n"
        "2. Medium (5 chances)\n"
        "3. Hard (3 chances)\n"
        "Enter your choice (1-3): "
    )
    while difficulty_choice not in ['1', '2', '3']:
        difficulty_choice = input("Invalid choice. Please enter 1, 2, or 3: ")

    difficulties = {'1': ('Easy', 10), '2': ('Medium', 5), '3': ('Hard', 3)}
    difficulty, max_attempts = difficulties[difficulty_choice]
    print(f"\nYou chose {difficulty} difficulty with {max_attempts} chances.\n")

    # Game setup
    secret_number = random.randint(1, 100)
    attempts = 0
    hint_counter = 0
    start_time = time.time()

    # Game loop
    while attempts < max_attempts:
        remaining_attempts = max_attempts - attempts
        print(f"Attempts left: {remaining_attempts}")
        guess = get_valid_guess()
        attempts += 1

        if guess == secret_number:
            time_taken = time.time() - start_time
            print(f"\n🎉 Congratulations! You guessed it in {attempts} attempts!")
            print(f"⏱️ Time taken: {time_taken:.1f} seconds")

            # Update high score
            if high_scores[difficulty] is None or attempts < high_scores[difficulty]:
                high_scores[difficulty] = attempts
                print("🏆 New high score!")
            return  # Exit after successful guess

        # Provide feedback
        if guess < secret_number:
            print("⬆️ The number is higher!")
        else:
            print("⬇️ The number is lower!")

        # Provide hints after every 2 attempts
        if attempts % 2 == 0 and hint_counter < 3:
            print(provide_hint(secret_number, hint_counter))
            hint_counter += 1

    # If all attempts exhausted
    time_taken = time.time() - start_time
    print(f"\n❌ Game Over! The number was {secret_number}.")
    print(f"⏱️ Time taken: {time_taken:.1f} seconds")

def main():
    """Main function to control game sessions."""
    while True:
        play_game()

        # Show high scores
        print("\n🏅 Current High Scores:")
        for level, score in high_scores.items():
            print(f"{level}: {score if score else '---'}")

        # Play again prompt
        replay = input("\nPlay again? (y/n): ").lower()
        while replay not in ['y', 'n']:
            replay = input("Please enter 'y' or 'n': ").lower()
        if replay == 'n':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
