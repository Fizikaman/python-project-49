import random

OPERATIONS = ['+', '-', '*']
RULES = 'What is the result of the expression?'


def generate_question_and_answer():
    answer = ''
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    operation = random.choice(OPERATIONS)
    question = f"{num1} {operation} {num2}"
    if operation == '+':
        answer = str(num1 + num2)
    elif operation == '-':
        answer = str(num1 - num2)
    elif operation == '*':
        answer = str(num1 * num2)
    return question, answer
