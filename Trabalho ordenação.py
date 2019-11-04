import random

n = int(input('Digite o número de elementos para ordenar: '))

lista = []
for i in range (n):
    lista.append(random.randint(0,100))

flag = 0
while flag == 0:
    flag = 1
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            lista[i], lista[i+1] = lista[i+1], lista[i]
            flag = 0     
print(lista)

            
    