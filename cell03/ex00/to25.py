#!/usr/bin/env python3
'''Exercicio 3.0 '''

try:
    number = int(input('Enter a number less than 25: \n'))    
    if number > 25:
        print('Error')    
    else:
        for i in range(number, 25 + 1):
            print(f'Inside the loop, my variable is {i}')
except ValueError:
    print('invalid value')

