#!usr/bin/env python3


import brain_games.games.cli
import brain_games.games.progression
import brain_games.games.run


def main():
    game = brain_games.games.progression
    brain_games.games.run.answer_from_user(game)


if __name__ == '__main__':
    main()
