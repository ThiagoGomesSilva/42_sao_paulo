#!/usr/bin/env python3
'''Exercicio 2.3 '''

num1 = int(input("Enter the first number: \n"))
num2 = int(input("Enter the second number: \n"))

result = num1 * num2

print(f'{num1} x {num2} = {result}')

if result == 0:
    print("The result is positive and negative.")
else:
    if (num1 * num2) > 0:
        print("The result is positive.")
    else:
        print("The result is negative.")
