import random

MIN_LENGTH = 5
MAX_LENGTH = 10
MIN_STEP = 1
MAX_STEP = 10
MIN_START = 1
MAX_START = 20

HIDDEN_PLACEHOLDER = ".."

DESCRIPTION = "What number is missing in the progression?"


def generate_arithmetic_progression(
    start: int,
    step: int,
    length: int,
) -> list[int]:
    return [start + i * step for i in range(length)]


def get_round() -> tuple[str, str]:
    length = random.randint(MIN_LENGTH, MAX_LENGTH)
    step = random.randint(MIN_STEP, MAX_STEP)
    start = random.randint(MIN_START, MAX_START)
    hidden_idx = random.randint(0, length - 1)

    terms = generate_arithmetic_progression(start, step, length)
    hidden_value = terms[hidden_idx]

    parts: list[str] = []
    for i, value in enumerate(terms):
        if i == hidden_idx:
            parts.append(HIDDEN_PLACEHOLDER)
        else:
            parts.append(str(value))

    question = " ".join(parts)
    return question, str(hidden_value)
