import prompt


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.TARGET_OF_GAME)
    n = 1
    while n <= 3:
        question, right_answer = game.generate_question_and_answer()
        print("Question: " + str(question))
        answer = prompt.string("Your answer: ")
        if answer != str(right_answer):
            print("'" + answer + "'" + " is wrong answer ;(.", end=" ")
            print("Correct answer was '" + str(right_answer) + "'.")
            print("Let's try again, " + name + "!")
            return
        else:
            print('Correct!')
            n += 1
    print('Congratulations, ' + name + '!')
