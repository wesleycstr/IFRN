#Faça um programa em PYTHON que receba um conjunto de valores numéricose que calcule e mostre o 
#maior e o menor valor do conjunto. Considere quepara encerrar a entrada de dados deve ser digitado o valor zero

Lista_valores = []
cond = True
while cond == True:
    valor = float(input('Digite um valor: '))
    if valor != 0:
        cond = True
        Lista_valores.append (valor)
    else:
        cond = False
print ('O maior valor digitado é: ',(max(Lista_valores)))
print ('O menor valor digitado é: ',(min(Lista_valores)))