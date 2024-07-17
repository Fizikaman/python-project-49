import random

from brain_games.services import generate_progression

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question_and_answer():
    start = random.randint(1, 10)
    step = random.randint(1, 10)
    length = random.randint(5, 10)
    progression = generate_progression(start, step, length)
    hidden_index = random.randint(0, length - 1)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = '..'
    question = ' '.join(map(str, progression))
    return question, correct_answer
