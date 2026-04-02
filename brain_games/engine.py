from collections.abc import Callable
from dataclasses import dataclass

import prompt

ROUNDS = 3

RoundPair = tuple[str, str]
GetRound = Callable[[], RoundPair]
IsCorrect = Callable[[str, str], bool]


@dataclass(frozen=True, slots=True)
class Game:
    description: str
    get_round: GetRound
    is_correct: IsCorrect


def run_game(game: Game) -> None:
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(game.description)

    for _ in range(ROUNDS):
        question, correct = game.get_round()
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")

        if not game.is_correct(answer, correct):
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct}'."
            )
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")
