#!/usr/bin/env python3
'''Exercicio 7.2 '''

def average(method1):
    total_sum = sum(method1.values())
    num_students = len(method1)
    return total_sum / num_students
    
    
class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}
class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}

print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")
