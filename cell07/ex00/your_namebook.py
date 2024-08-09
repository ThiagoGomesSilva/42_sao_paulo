#!/usr/bin/env python3
'''Exercicio 7.0 '''

def array_of_names(param1):    
    full_name = []
    for first_name, last_name in param1.items():
        list = f'{first_name.capitalize()} {last_name.capitalize()}'
        full_name.append(list)
    return full_name

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}

print(array_of_names(persons))