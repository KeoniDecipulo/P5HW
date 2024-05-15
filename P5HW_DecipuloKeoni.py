# Your Name
# Date
# Assignment Name: Math Quiz
# Brief description of program: A menu-driven program that allows the user to add or subtract random numbers.

import random

def generate_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return num1, num2

def add_numbers(num1, num2):
    return num1 + num2

def subtract_numbers(num1, num2):
    return num1 - num2

def main():
    print("Welcome to Math Quiz\n")
    choice = 0
    while choice != 3:
        print("MAIN MENU")
        print("-----------------------")
        print("1. Adding Random Numbers")
        print("2. Subtracting Random Numbers")
        print("3. Exit\n")
        choice = int(input("Please choose one of the main options: "))
        if choice == 1:
            num1, num2 = generate_numbers()
            result = add_numbers(num1, num2)
            guess = None
            while guess != result:
                guess = int(input(f"What is the sum of {num1} and {num2}? "))
                if guess < result:
                    print("Sorry, guess is too low. Try again.")
                elif guess > result:
                    print("Sorry, guess is too high. Try again.")
                else:
                    print("Congratulations! You guessed correctly.")
        elif choice == 2:
            num1, num2 = generate_numbers()
            result = subtract_numbers(num1, num2)
            guess = None
            while guess != result:
                guess = int(input(f"What is {num1} minus {num2}? "))
                if guess < result:
                    print("Sorry, answer is too low. Try again.")
                elif guess > result:
                    print("Sorry, answer is too high. Try again.")
                else:
                    print("Congratulations! You guessed correctly.")
        elif choice == 3:
            print("Thank you for playing...")
            print('Bye!!')
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
