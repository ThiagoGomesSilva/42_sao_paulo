#!/usr/bin/env python3
'''Exercicio 7.3 '''

def famous_births(param):
    if "date_of_birth" == True:
        order_years = sorted(param.keys())
    else:
        False
    return order_years

women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

print(famous_births(women_scientists))
