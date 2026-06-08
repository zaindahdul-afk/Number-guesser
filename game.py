import random


def play():
    number = random.randint(1, 100)
    attempts = 0

    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        attempts += 1

        if guess < number:
            print("Higher!")
        elif guess > number:
            print("Lower!")
        else:
            print(f"Correct! You got it in {attempts} guess{'es' if attempts != 1 else ''}.")
            break


if __name__ == "__main__":
    play()
