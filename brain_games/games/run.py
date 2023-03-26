import prompt


def answer_from_user(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    game.start_game()
    n = 1
    while n <= 3:
        question, right_answer = game.game_logic()
        print("Question: " + str(question))
        answer = prompt.string("Your answer: ")
        if answer != str(right_answer):
            print("'" + answer + "'" + " is wrong answer ;(. Correct answer was '" + str(right_answer) + "'.\nLet\'s try again, " +name + "!")
            return
        else:
            print('Correct!')
            n += 1
    print('Congratulations, ' + name + '!')    
