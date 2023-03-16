#!/usr/bin/env python3


import brain_games.cli
import brain_games.even
def main():
    brain_games.cli.welcome_user()
    brain_games.even.start_game()
    brain_games.even.answer_from_user()


if __name__ == '__main__':
        main()
