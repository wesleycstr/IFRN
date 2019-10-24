#Dada uma lista A com m linhas e n colunas (onde m e n serão valores informados no teclado)
#e onde os valores dessa lista deverão ser reais entre 1 e 10 gerados aleatoriamente e uma lista
#V com n elementos (onde n será um valor informado no teclado) e onde os valores deverão ser
#reais entre 1 e 10 gerados aleatoriamente, determinar o produto de A por V.

import random

while True:
    linhas_a = int(input('Digite o número de linhas para a matriz A: '))
    colunas_a = int(input('Digite o número de colunas para a matriz A: '))
    print()
    n = int(input('Digite o número de elementos para a matriz B: '))

    #Aceitando somente quantidades possíveis para a matriz B
    if n % colunas_a != 0:
        r = n // colunas_a
        print('-='*80)
        print ('Para que seja possível multiplicar a matriz A pela matriz B é necessário que o número de elementos de B seja um múltiplo do número de colunas da matriz A.')
        print('-='*80)
        continue
    else:
        break

#Gerando a matriz A    
matriz_a = []                      
for i in range(linhas_a):          
    linha = []                     
    for j in range(colunas_a):
        linha.append(random.randint(1,10))                      
    matriz_a.append(linha)
print('-='*80)
print ('A matriz A é uma matriz {}x{} com os seguintes elementos: {}'.format(linhas_a,colunas_a,matriz_a))
print('-='*80)

#Adequando a matriz B para que seja possivel exercer uma multiplicação
linhas_b = colunas_a
colunas_b = int(n / colunas_a)

#Gerando a matriz B
matriz_b = []                      
for i in range(linhas_b):          
    linha_2 = []                     
    for j in range(colunas_b):
        linha_2.append(random.randint(1,10))                      
    matriz_b.append(linha_2)
print ('A matriz B é uma matriz {}x{} com os seguintes elementos: {}'.format(linhas_b,colunas_b,matriz_b))
print('-='*80)

#Multiplicando as matrizes
resultado = []
for i in range (linhas_a):
    resultado.append([])
    for j in range (colunas_b):
        resultado[i].append(0)
        for k in range (colunas_a):
            resultado[i][j] += matriz_a[i][k] * matriz_b[k][j]
print()
print ('O resultado da multiplicação da matriz A pela matriz B é uma matriz {}x{} com os seguintes elementos: {}'.format(linhas_a,colunas_b,resultado))
print()
print()