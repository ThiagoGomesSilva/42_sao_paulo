#!/usr/bin/env python3
'''Exercicio 4.2 '''

try:
    num1 = int(input('Give me the first number: '))
    num2 = int(input('Give me the second number: '))
    
    print('Thank you!')
    print(f'{num1} + {num2} = {num1 + num2}')
    print(f'{num1} - {num2} = {num1 - num2}')
    print(f'{num1} / {num2} = {num1 // num2}')
    print(f'{num1} * {num2} = {num1 * num2}')
except ValueError:
    print('Invalid value')