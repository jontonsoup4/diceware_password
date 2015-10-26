import random

f = open('wordlist.txt').readlines()
pass_dict = {}
for line in f:
    pass_dict[line[:5]] = line[6:].strip('\n')


def roll_dice():
    dice = []
    for _ in range(5):
        dice.append(random.randint(1, 6))
    return pass_dict[''.join(str(n) for n in dice)]


def generate(num=1):
    for word in range(num):
        word_list = []
        for _ in range(6):
            word_list.append(roll_dice())
        print(' '.join(word_list))


if __name__ == '__main__':
    generate(int(input('How many passwords to generate? ')))
