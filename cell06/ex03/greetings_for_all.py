#!/usr/bin/env python3
'''Exercicio 6.3 '''

import sys

def greetings(name="noble stranger"):
        if name == '':
            return f'Hello, noble stranger.'
        elif not isinstance(name, str):
            return f'Error! It was not a name.'
        else:
            return f'Hello, {name}'

print(greetings('Alexandra'))
print(greetings('Wil'))
print(greetings())
print(greetings(42))
