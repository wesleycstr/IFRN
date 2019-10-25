#Faça um programa em PYTHON que leia vários inteiros positivos e mostre, no final, a soma dos números pares e a soma dos números ímpares.
#O programa deverá ser encerrado quando for digitado o valor zero.

soma_par = 0
soma_impar = 0
leitura = 'true'

while leitura == 'true':
    numero = int(input('Digite um número: '))
    if numero == 0:
        leitura = 'false'
    else:
        if numero % 2 == 0:
            soma_par = soma_par + numero
        else:
            soma_impar = soma_impar + numero
print ('Valor da soma dos números pares: ',soma_par)
print ('Valor da soma dos números impares: ',soma_impar)