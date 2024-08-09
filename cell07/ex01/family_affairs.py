#!/usr/bin/env python3
'''Exercicio 7.1 '''

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

def find_the_redheads(color):    
    if color == 'red':
        return color == 'red'
    else:
        return False  

full_family = list(filter(lambda name: find_the_redheads(dupont_family[name]), dupont_family.keys()))

print(full_family)
