#!usr/bin/env python3


import brain_games.games.gcd
import brain_games.games.run


def main():
    game = brain_games.games.gcd
    brain_games.games.run.answer_from_user(game)


if __name__ == '__main__':
    main()
