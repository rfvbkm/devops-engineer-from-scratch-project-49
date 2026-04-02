import random

import prompt

ROUNDS = 3
MIN_NUMBER = 1
MAX_NUMBER = 100


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(ROUNDS):
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        print(f"Question: {number}")
        answer = prompt.string("Your answer: ")

        correct = "yes" if number % 2 == 0 else "no"
        if answer not in ("yes", "no") or answer != correct:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct}'."
            )
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
