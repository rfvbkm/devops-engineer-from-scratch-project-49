from collections.abc import Callable
from types import ModuleType

import prompt

ROUNDS = 3

RoundPair = tuple[str, str]
GetRound = Callable[[], RoundPair]

YES_OR_NO = ("yes", "no")


def is_answer_correct(answer: str, correct: str) -> bool:
    if correct in YES_OR_NO:
        return answer in YES_OR_NO and answer == correct
    return answer == correct


def welcome_user() -> str:
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def run_game(game: ModuleType) -> None:
    name = welcome_user()
    print(game.DESCRIPTION)

    for _ in range(ROUNDS):
        question, correct = game.get_round()
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")

        if not is_answer_correct(answer, correct):
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct}'."
            )
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")
