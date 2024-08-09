#!/usr/bin/env python3
'''Exercicio 7.3 '''

def famous_births(param):
    
    figures = sorted(param.items(), key=lambda item: item[1]['date_of_birth'])

    for key, details in figures:
        print(f"Name: {details['name']}, Date of Birth: {details['date_of_birth']}")

women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)
