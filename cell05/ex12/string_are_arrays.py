#!/usr/bin/env python3
'''Exercicio 5.12 '''

import sys

letter = 'z'
arguments = sys.argv[1:]

for i in arguments:
    letter_user = i.count(letter)
    count = len(i)
    if count > 1:
        print(f'{letter_user}')
    elif count == letter_user:
        print(f'{letter_user}')
    else:
        print('none')