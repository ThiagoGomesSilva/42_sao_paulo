#!/usr/bin/env python3
'''Exercicio 5.12 '''

import sys
            
def main():
    # Check the number of command-line arguments
    if len(sys.argv) != 2:
        print("none")
        return
    
    input_string = sys.argv[1]
    
    found_z = False
    for char in input_string:
        if char == 'z':
            print('z', end = '')
            found_z = True
    
    if not found_z:
        print("none")

if __name__ == "__main__":
    main()