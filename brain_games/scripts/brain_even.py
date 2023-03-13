#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.even import answer_from_user
main()
welcome_user()
print('Answer "yes" if the number is even, otherwise answer "no".')
answer_from_user()

if __name__ == '__main__':
        main()
