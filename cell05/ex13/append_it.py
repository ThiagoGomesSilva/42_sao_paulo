#!/usr/bin/env python3
'''Exercicio 5.13 '''

import sys

arguments = sys.argv[1:]

if not arguments:
    print('none')

for arg in arguments:
    if not arg.endswith('ism'):
        print(arg + 'ism')
