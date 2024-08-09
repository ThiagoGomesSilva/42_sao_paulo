#!/usr/bin/env python3
'''Exercicio 6.2 '''

import sys

def downcase_it(*args):
    arguments = sys.argv[1:]
    x = []
    if len(arguments) > 0:        
        for arg in arguments:
            x.append(arg.lower())
        x = " \n".join(x) # Com o JOIN conseguimos converter um array em string e o que inserirmos dentro dos parenteses será usado após cada parametro informado
        return x
    else:
        return 'none'

print(downcase_it())
