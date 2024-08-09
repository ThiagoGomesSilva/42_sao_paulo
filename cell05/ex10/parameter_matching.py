#!/usr/bin/env python3
'''Exercicio 5.10 '''
import sys

if len(sys.argv) < 2:
    print('none')
else:
    name = input('What was the parameter?')
    if name == "Hello":
        print('Good job!')
    else:
        print('Nope, sorry...')

