#!/usr/bin/env python3
'''Exercicio 5.11 '''

import sys

if len(sys.argv) < 2:
    print('none')

else:
    arguments = sys.argv[1:]
    print(f'parameters: {len(arguments)}')
    for i in arguments:
        print(f'{i}: {len(i)}')
