import random

from brain_games.services import is_even

RULES = 'Answer "yes" if the number is even, otherwise answer "no"'


def generate_question_and_answer():
    number = random.randint(1, 100)
    question = number
    correct_answer = "yes" if is_even(number) else "no"

    return question, correct_answer
