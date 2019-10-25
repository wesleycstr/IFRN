#Faça um programa em PYTHON que receba um conjunto de valores numéricos e que 
#calcule e mostre o maior e o menor valor do conjunto. Considere quepara encerrar 
#a entrada de dados deve ser digitado o valor zero

valor = float(input('Digite um valor: '))
menor = valor
maior = valor
leitura = 'true'

while leitura == 'true':
    valor = float(input('Digite um valor: '))
    if valor == 0:
        leitura = 'false'
    else:
        if valor > maior:
            maior = valor
        elif valor < menor:
            menor = valor
print ('Menor valor: ',menor)
print ('Maior valor: ',maior)