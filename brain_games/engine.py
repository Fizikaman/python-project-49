import prompt

ROUNDS = 3


def play_game(game, name):
    print('-' * 80)
    print(game.RULES)
    print('-' * 80)

    for _ in range(ROUNDS):
        question, correct_answer = game.generate_question_and_answer()
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")

        if answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
