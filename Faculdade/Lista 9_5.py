#Dada uma lista A com m linhas e n colunas (onde me n serão valores informados no teclado) 
#e onde os valores dessa lista deverão ser reais entre 1 e 10 gerados aleatoriamente e 
#uma lista V com n elementos (onde n será um valor informado no teclado) e onde os valores
#deverão ser reais entre 1 e 10 gerados aleatoriamente, determinar o produto de Apor V.

import random
linhas_A = int(input('Digite o número de linhas da matriz A: '))
colunas_A = int(input('Digite o número de colunas da matriz A: '))
matriz_A = []

for i in range (linhas_A):
    sub_matriz = []
    for j in range (colunas_A):
        sub_matriz.append(random.randrange(1,11))
    matriz_A.append(sub_matriz)
print (matriz_A)
