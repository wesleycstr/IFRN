#Dada uma lista A com m linhas e n colunas (onde m e n serão valores informados no teclado)
#e onde os valores dessa lista deverão ser reais entre 1 e 10 gerados aleatoriamente e uma lista
#V com n elementos (onde n será um valor informado no teclado) e onde os valores deverão ser
#reais entre 1 e 10 gerados aleatoriamente, determinar o produto de A por V.

import random

while True:
    linha = int(input('Digite o número de linhas para a matriz A: '))
    coluna = int(input('Digite o número de colunas para a matriz A: '))
    print()
    n = int(input('Digite o número de elementos para a matriz B: '))

    if n % coluna != 0:
        r = n // coluna
        print (r)
        print ('Para que seja possível multiplicar a matriz A pela matriz B é necessário que o número de elementos de B seja um múltiplo de {}'.format(coluna))
        continue
    else:
        break