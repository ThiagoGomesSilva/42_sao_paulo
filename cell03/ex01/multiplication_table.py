#!/usr/bin/env python3
'''Exercicio 3.1 '''

try:
    range_values = int(input('Enter a number: \n'))    
    for i in range(0, 10):
        print(f'{i} x {range_values} = {i * range_values}')
except ValueError:
    print('Invalid value')
