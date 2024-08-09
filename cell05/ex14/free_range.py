#!/usr/bin/env python3
'''Exercicio 5.14 '''

import sys

arguments = sys.argv[1:]

try:
    if len(arguments) != 2:
        print('none')
    else:    
        start = int(arguments[0])
        end = int(arguments[1])
        list = []
            
        for i in range(start, end + 1):
            list.append(i)            
        print(list)
except ValueError:
    print('Invalid value')