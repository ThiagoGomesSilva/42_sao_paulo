#!/usr/bin/env python3
'''Exercicio 2.2 '''

password = "Python é incrível"

password_user = input('Insert password: ')

if password_user == password:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")