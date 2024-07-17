import prompt
from brain_games.games import even, calc, gcd, progression, prime
from brain_games.engine import play_game


def welcome():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name?\n")
    print(f"Hello, {name}!")
    return name


def choose_game():
    print("Please choose a game:\n"
          "1 - Even\n"
          "2 - Calculator\n"
          "3 - NOD\n"
          "4 - Progression\n"
          "5 - Is_prime")
    choice = prompt.string("Your choice: ")
    return choice


def launch_game(choice, name):
    games = {
        "1": even,
        "2": calc,
        "3": gcd,
        "4": progression,
        "5": prime,
    }
    game = games.get(choice)
    if game:
        play_game(game, name)
    else:
        print("Invalid choice. Please select a valid game number.")


def main():
    name = welcome()
    choice = choose_game()
    launch_game(choice, name)


if __name__ == '__main__':
    main()
