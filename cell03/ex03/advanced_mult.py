#!/usr/bin/env python3
'''Exercicio 3.3 '''
import sys

contador1 = 0
contador2 = 1
numero = 10

if len(sys.argv) > 1:
    print('none')
else:
    while contador1 <= numero:
        print(f'Table de {contador1}: ', end=" ")
        while contador2 <= numero:
            print(f'{contador1 * contador2}', end=" ")
            contador2 += 1
        contador1 += 1
        contador2 = 0
        print('')
