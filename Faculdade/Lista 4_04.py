#Faça  um programa  em  PYTHON que  calcule a somados  números positivos digitados  pelo usuário.  
#O algoritmo deve  permitir  que  o usuário  digite  uma  quantidade  não  determinada  de números. 
#O algoritmo encerra e imprime o valor da soma quando o usuário digita o valor zero.

soma = 0
leitura = 'true'

while leitura == 'true':
    numero = float(input('Digite o número: '))
    if numero == 0:
        leitura = 'false'
    else:
        if numero > 0:
            soma = numero + soma
print (soma)
