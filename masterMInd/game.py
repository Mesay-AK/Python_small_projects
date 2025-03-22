import random

COlORS = ['R', 'G', 'B', 'Y', 'W', 'O']
TRIES = 10
CODE_LENGTH = 4

def generate_code():
    code = []

    for _ in range(CODE_LENGTH):
        color = random. choice(COlORS)
        code.append(color)

    return code

code = generate_code()

def guess_code():
    
    guess = input('Guess:  ').upper().split("")

    if len(guess) != CODE_LENGTH:
        print(f'You must guess {CODE_LENGTH} colors.')
        return guess_code()
    
    for color in guess:
        if color not in COlORS:
            print(f'Invalid color :  {color}.')
            return guess_code()

    return guess

