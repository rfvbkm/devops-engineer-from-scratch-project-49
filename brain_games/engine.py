from collections.abc import Callable
from typing import TypeAlias

import prompt

ROUNDS = 3

RoundPair = tuple[str, str]
GetRound = Callable[[], RoundPair]

Game: TypeAlias = tuple[str, GetRound]

YES_OR_NO = ("yes", "no")


def is_answer_correct(answer: str, correct: str) -> bool:
    if correct in YES_OR_NO:
        return answer in YES_OR_NO and answer == correct
    return answer == correct


def run_game(game: Game) -> None:
    description, get_round = game
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(description)

    for _ in range(ROUNDS):
        question, correct = get_round()
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
