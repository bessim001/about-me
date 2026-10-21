import random


def play(low: int = 1, high: int = 100) -> None:
    secret = random.randint(low, high)
    attempts = 0
    print(f"I'm thinking of a number between {low} and {high}.")

    while True:
        guess = input("Your guess: ").strip()
        if not guess.lstrip("-").isdigit():
            print("Please enter a whole number.")
            continue

        attempts += 1
        number = int(guess)
        if number < secret:
            print("Too low!")
        elif number > secret:
            print("Too high!")
        else:
            print(f"Correct! You got it in {attempts} tries.")
            break


if __name__ == "__main__":
    play()
