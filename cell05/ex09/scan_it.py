#!/usr/bin/env python3
'''Exercicio 5.9 '''

import sys
import re

arguments = sys.argv[1:]

if len(arguments) != 2:
    print('none')
else:
    param1 = arguments[0]
    param2 = arguments[1]
    verify = len(re.findall(param1, param2))
    if verify > 0:
        print(verify)
    else:
        print('none')
