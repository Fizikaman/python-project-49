from brain_games.engine import play_game
from brain_games.games import even
from brain_games.games.launcher import welcome


def main():
    name = welcome()
    play_game(even, name)


if __name__ == "__main__":
    main()
