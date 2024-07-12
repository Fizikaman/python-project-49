import random

from brain_games.services import is_even

RULES = ('Суть игры в следующем: вам показывается случайное число.\n'
         'Нужно ответить yes, если число чётное, или no — если нечётное.\n'
         'Любой некорректный ввод считается ошибкой, например, n, и '
         'равносилен неправильному ответу;)')


def generate_question_and_answer():
    number = random.randint(1, 100)
    question = number
    correct_answer = "yes" if is_even(number) else "no"

    return question, correct_answer
