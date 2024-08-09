#!/usr/bin/env python3
'''Exercicio 5.2 '''

lista = [2, 8, 9, 48, 8, 22, -12, 2]
new_list = []
print(f'Original array: {lista}')

for list in lista:
    if list > 5:
        soma = list + 2
        new_list.append(soma)
print(f'New array: {new_list}')
