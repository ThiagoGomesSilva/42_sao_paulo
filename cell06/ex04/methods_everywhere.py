#!/usr/bin/env python3
'''Exercicio 6.4 '''

import sys


def shrink(s):    
    print(s[:8]) # Recebe os 8 primeiros caracteres da string.

def enlarge(s):    
    print(s.ljust(8, 'Z')) # Insere caracteres 'Z' até completar oito caracteres e exibe o resultado.

def main():
    # Verifica se é menor que o parametro 2, caso seja menor retornar none pois o primeiro parametro é o nome do arquivo.
    if len(sys.argv) < 2:
        print('none')
        return

    # Verifica a partir do que recebemos no 2º parametro e realizamos as validações conforme proposto no desafio
    for arg in sys.argv[1:]:
        if len(arg) > 8: # Se for maior que 8 chamamos o metodo shrink retornando somente os 8 primeiros caracteres
            shrink(arg)
        elif len(arg) < 8: # Se for menor que 8 chamamos o metodo enlarge que preenche com 'Z' até completar 8 posições
            enlarge(arg)
        else:
            print(arg)
            
if __name__ == "__main__":
    main()
