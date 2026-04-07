import math
import random

MIN_NUMBER = 1
MAX_NUMBER = 100

DESCRIPTION = "Find the greatest common divisor of given numbers."


def get_round() -> tuple[str, str]:
    a = random.randint(MIN_NUMBER, MAX_NUMBER)
    b = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = f"{a} {b}"
    correct = str(math.gcd(a, b))
    return question, correct


GAME = (DESCRIPTION, get_round)
