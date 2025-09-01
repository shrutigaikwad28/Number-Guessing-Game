import random
import time

def choose_difficulty():
    print("Choose difficulty level:")
    print("1. Easy (1–10, 5 guesses)")
    print("2. Medium (1–50, 7 guesses)")
    print("3. Hard (1–100, 10 guesses)")
    
    while True:
        choice = input("Enter 1, 2, or 3: ")
        if choice == '1':
            return 10, 5
        elif choice == '2':
            return 50, 7
        elif choice == '3':
            return 100, 10
        else:
            print("Invalid choice. Try again.")

def calculate_score(attempts_used, max_attempts, time_taken):
    base_score = 100
    efficiency_bonus = (max_attempts - attempts_used) * 10
    time_penalty = int(time_taken) // 2  # 1 point off every 2 seconds
    final_score = max(base_score + efficiency_bonus - time_penalty, 0)
    return final_score

def play_game():
    max_number, max_attempts = choose_difficulty()
    secret_number = random.randint(1, max_number)
    print(f"\nI'm thinking of a number between 1 and {max_number}. You have {max_attempts} attempts!")

    start_time = time.time()
    for attempt in range(1, max_attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}: Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess == secret_number:
            end_time = time.time()
            time_taken = end_time - start_time
            score = calculate_score(attempt, max_attempts, time_taken)
            print(f"\n🎉 Correct! You guessed it in {attempt} tries and {int(time_taken)} seconds.")
            print(f"🏆 Your score: {score}")
            break
        elif guess < secret_number:
            print("Too low.")
        else:
            print("Too high.")
    else:
        end_time = time.time()
        time_taken = end_time - start_time
        print(f"\n😢 Out of attempts! The number was {secret_number}.")
        print(f"⏱ You took {int(time_taken)} seconds.")

play_game()
