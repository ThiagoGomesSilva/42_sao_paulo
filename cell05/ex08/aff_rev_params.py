#!/usr/bin/env python3
'''Exercicio 5.8 '''

import sys

# if len(sys.argv) != '' and len(sys.argv) > 2:
#     print(f'{sys.argv} \n')
# else:
#     print('none')
    
def main():
    # Obtém os parâmetros passados para o script, excluindo o nome do próprio script
    params = sys.argv[1:]

    # Verifica se há pelo menos dois parâmetros
    if len(params) < 2:
        print("none")
    else:
        # Imprime os parâmetros na ordem inversa, cada um seguido por uma nova linha
        for param in reversed(params):
            print(param)

if __name__ == "__main__":
    main()
