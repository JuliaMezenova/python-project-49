import prompt
import random
from brain_games.cli import welcome_user


def answer_from_user():
    name = welcome_user()
    start_game = 'Answer "yes" if the number is even, otherwise answer "no".'
    print(start_game)
    question = random.randint(1, 100)
    def is_right_answer(question):
        right_answer = ''  
        if question%2 == 0:
            right_answer = 'yes'
        else:
            right_answer = 'no'
        return right_answer
    print("Question: " + str(question))
    answer = prompt.string("Your answer: ")
    n = 1
    while answer == is_right_answer(question) and n < 3:
        print('Correct!')
        n+=1
        question = random.randint(1, 100)
        print("Question: " + str(question))
        answer = prompt.string("Your answer: ")
        is_right_answer(question)
    if answer != is_right_answer(question):
        print("'" + answer + "'" + " is wrong answer ;(. Correct answer was '" + is_right_answer(question) + "'.\nLet\'s try again, " + name + "!")
        print("")
    else:
        print('Congratulations, ' + name +'!')
