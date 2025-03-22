import random

COLORS = ['R', 'G', 'B', 'Y', 'W', 'O']
TRIES = 10
CODE_LENGTH = 4

def generate_code():
    code = []

    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)

    return code

code = generate_code()

def guess_code():
    
    guess = list(input('Guess:  ').upper())

    if len(guess) != CODE_LENGTH:
        print(f'You must guess {CODE_LENGTH} COLORS.')
        return guess_code()
    
    for color in guess:
        if color not in COLORS:
            print(f'Invalid color :  {color}.')
            return guess_code()

    return guess


def check_code(guess, real_code):
    color_counts = {}
    correct_position = 0
    incorrect_position = 0

    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    for guess_color, real_code in zip(guess, real_code):
        if guess_color == real_code:
            correct_position += 1
            color_counts[real_code] -= 1

    for guess_color, real_code in zip(guess, real_code):
        if guess_color != real_code and color_counts[real_code] > 0:
            incorrect_position += 1
            color_counts[real_code] -= 1

    return correct_position, incorrect_position


def game():
    print("Welcome to Mastermind!")
    print(f"You have {TRIES} tries to guess the code...")
    print("The COLORS are: ", *COLORS)
    code = generate_code()
    for attempts in range(1, TRIES + 1):
        print(f'Attempt {attempts}')
        guess = guess_code()
        correct_position, incorrect_position = check_code(guess, code)

        if correct_position == CODE_LENGTH:
            print(f'Congratulations! You guessed in {attempts}the code.')
            break

        print(f"Correct positons: {correct_position} | Incorrect positions: {incorrect_position}")

    else:
        print('You run out of tries. The code was ', *code)


if __name__ == '__main__':

    while True:
        game()
        play_again = input('Do you want to play again? (yes/no): ').lower()
        if play_again != 'yes':
            break
    