#!/usr/bin/python3
# -*- coding: utf-8 -*-
from random import choice
from json import dumps
from sys import argv
from constants import LEFT, RIGHT

totals = (len(LEFT), len(RIGHT))


def get(amount=1, separator='_', unique=False):
    if amount == 1:
        name = '{}{}{}'.format(choice(LEFT), separator, choice(RIGHT))

        if name == 'boring{}wozniak'.format(separator):
            # No way.
            return get(amount, separator, unique)

        return name

    names = []
    for i in range(0, amount):
        try:
            chosen_left = choice(LEFT)
            chosen_right = choice(RIGHT)
        except IndexError:
            print(
                '[WARN] Exhausted at least one source (you requested unique words and too many names)\nCurrently knowing {}'
                ' pretty adjectives and {} brilliant humans.\n'.format(*totals))
            return dumps(names)

        if unique:
            LEFT.remove(chosen_left)
            RIGHT.remove(chosen_right)

        names.append('{}{}{}'.format(chosen_left, separator, chosen_right))

    if 'boring{}wozniak'.format(separator) in names:
        # Unacceptable.
        names.remove('boring{}wozniak'.format(separator))
    return dumps(names)


if __name__ == '__main__':
    try:
        number = int(argv[1])
    except IndexError:
        number = 1

    print(get(number))
