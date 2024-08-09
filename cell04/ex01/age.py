#!/usr/bin/env python3
'''Exercicio 4.1 '''

user_age = int(input("Please tell me your age: "))
print(f'You are currently {user_age} years old. ')

count = 0
sum = 0

while count < 3:
    sum += 10
    print(f"In {sum} years, you'll be {sum + user_age} years old.")
    count += 1

