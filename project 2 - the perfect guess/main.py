# The perfect guess game

from random import randint as ri

def main():
    print("Welcome to the Perfect Guess Game!")
    n = ri(1, 100)
    guesses = 0

    while True:
        try:
            a = int(input("Guess the number: "))
            guesses += 1

            if a > n:
                print("Enter a lower number")
            elif a < n:
                print("Enter a higher number")
            else:
                print(f"Congratulations! You guessed the number {n} correctly in {guesses} guesses.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
main()