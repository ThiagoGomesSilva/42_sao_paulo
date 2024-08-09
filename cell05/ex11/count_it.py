#!/usr/bin/env python3
'''Exercicio 5.11 '''

import sys

arguments = sys.argv[1:]

for i in arguments:
    print(f'{i}: {len(i)}')
