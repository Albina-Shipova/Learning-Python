from random import randint

guess = ''


def number_guess():
    global guess
    guess = ''
    for _ in range(4):
        guess += str(randint(0, 9))


def check_number(input_number):
    bulls_count = 0
    cows_count = 0
    for i, n in enumerate(input_number):
        if n in guess:
            if n == guess[i]:
                bulls_count += 1
            else:
                cows_count += 1
    res = {
        'быки': bulls_count,
        'коровы': cows_count
    }
    return res


# number_guess()
# print(guess)
#
# print(check_number())
