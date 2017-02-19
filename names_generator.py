#!/usr/bin/python3
# -*- coding: utf-8 -*-
from random import choice
from json import dumps
from sys import argv, stdin
import os
from constants import LEFT, RIGHT
totals = (len(LEFT), len(RIGHT))

def make_name(s='_', u=False):
    chosen_left = choice(LEFT)
    chosen_right = choice(RIGHT)
    if u:
        LEFT.remove(chosen_left)
        RIGHT.remove(chosen_right)
    return '{}{}{}'.format(chosen_left, s, chosen_right)

def get(n=1, separator='_', unique=False):
    if n == 1:
        return make_name(separator, unique)

    names = []
    for i in range(n):
        try:
            names.append(make_name(separator, unique))
        except IndexError:
            print(
                 '[WARN] Exhausted at least one source (you requested unique words and too many names)\nCurrently knowing {} pretty adjectives and {} brilliant humans.\n'.format(*totals))
            return dumps(names)

    if 'boring{}wozniak'.format(separator) in names:
        # Unacceptable.
        names.remove('boring{}wozniak'.format(separator))
    print('Content-type: application/json')
    return dumps(names)


if __name__ == '__main__':
    print("HTTP/1.0 200 OK")
    n = os.getenv('QUERY_STRING')
    try: 
        n = int(n)
    except ValueError:
        n = 1
    print(get(n))
