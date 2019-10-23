#Lista_9 Questão_02, Por Wesley Castro

#Gerar uma lista de dimensão de n (onde n será um valor informado no teclado) elementos, com
#os elementos na faixa dos números inteiros entre 0 e 99 (inclusive), gerados aleatoriamente.
#Determinar qual o elemento que foi mais sorteado e o elemento que foi menos sorteado.

#Início: Importando biblioteca
import random                                                       
#Fim: Importando biblioteca

#Início: Recebendo número de elementos
print('')                                                                  
n = int(input('Digite a quantidade de elementos: '))
#Fim: Recebendo número de elementos

#Início: Gerando números aleatórios                                                          
lista = []                                                         
for contador in range(0, n):
    lista.append(random.randint(0, 99))
#Início: Gerando números aleatórios                     

#Início: Exibindo valores gerados em ordem crescente                               
print ('')
lista.sort()
print ('=-'*40)                                                        
print ('Lista gerada aleatóriamente:',lista)                        
print ('=-'*40)         
#Fim: Exibindo valores gerados em ordem crescente  
        

#Inicio: Limpando a lista retirando os elementos repetidos
lista_sem_repetições = []
for i in lista:
    if i not in lista_sem_repetições:
        lista_sem_repetições.append(i)
#Fim: Limpando a lista retirando os elementos repetidos


#Início: Contar o número de ocorrências de repetições
lista_contador = []
for numero in lista_sem_repetições:
    lista_contador.append(lista.count(numero))
#Fim: Contar o número de ocorrências de repetições
   
#Início: Eliminando os números que apareceram apenas uma vez
lista_qtd_repetições = []
lista_repetidos = []
for i in lista_contador:
    if i != 1:
        endereço = lista_contador.index(i)
        lista_qtd_repetições.append(i)
        lista_repetidos.append(lista_sem_repetições[endereço])
        lista_sem_repetições.pop(endereço)
        lista_contador.pop(endereço)
#Fim: Eliminando os números que apareceram apenas uma vez

#Início: Finalizando o programa em caso de não repetição
if lista_qtd_repetições == []:
    print ('Não ocorreram repetições!')
#Fim: Finalizando o programa em caso de não repetição

#Início: Continuando o programa em caso de repetição
else:
    #Início: Verificando o que mais se repete
    mais_repetido = max(lista_qtd_repetições)
    lista_mais_repetidos = []
    for i in range (len(lista_qtd_repetições)):
        if lista_qtd_repetições[i]==mais_repetido:
            lista_mais_repetidos.append(lista_repetidos[i])
    #Fim: verificando o que mais se repete

    #Início: Verificando o que menos se repete
    menos_repetido = min(lista_qtd_repetições)
    lista_menos_repetidos = []
    for i in range (len(lista_qtd_repetições)):
        if lista_qtd_repetições[i]==menos_repetido:
            lista_menos_repetidos.append(lista_repetidos[i])
    #Fim: verificando o que menos se repete

    #Início: Apresentando os resultados:
    if mais_repetido == menos_repetido:
        print ('Número(s) mais repetido(s): {}. Quantidade de repetição: {}. Não houve outras ocorrências de repetição!'.format(lista_mais_repetidos, mais_repetido))
    else:
        print ('Número(s) mais repetido(s): {}. Quantidade de repetições: {}.'.format(lista_mais_repetidos, mais_repetido))
        print ('Número(s) menos repetido(s): {}. Quantidade de repetições: {}.'.format(lista_menos_repetidos, menos_repetido))
    #Fim: Apresentando os resultados:
#Fim: Continuando o programa em caso de repetição