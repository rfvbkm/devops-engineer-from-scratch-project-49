import random

MIN_NUMBER = 1
MAX_NUMBER = 100
OPERATORS = ("+", "-", "*")

DESCRIPTION = "What is the result of the expression?"


def get_round() -> tuple[str, str]:
    left = random.randint(MIN_NUMBER, MAX_NUMBER)
    right = random.randint(MIN_NUMBER, MAX_NUMBER)
    op = random.choice(OPERATORS)
    match op:
        case "+":
            result = left + right
        case "-":
            result = left - right
        case "*":
            result = left * right
        case _:
            raise AssertionError(f"unknown operator: {op!r}")
    question = f"{left} {op} {right}"
    return question, str(result)


def is_correct(answer: str, correct: str) -> bool:
    return answer == correct
