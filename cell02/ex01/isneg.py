#!/usr/bin/env python3
'''Exercicio 2.1 '''

numero = int(input('Digite um numero: '))

if numero == 0:
    print("Este número é tanto positivo quanto negativo.")
elif numero > 0:
    print("Este número é positivo.")
else:
    print("Este número é negativo.")