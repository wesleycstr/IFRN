#Faça um programa que recebe a idade de 15 pessoas e que imprima no final (utilize o método
#FORMAT) os dados conforme modelo abaixo.

#FAIXA ETÁRIA        TOTAL       %
#Até 15 anos         x           n.n    (1)
#De 16 a 30 anos     x           n.n    (2)
#De 31 a 45 anos     x           n.n    (3)
#De 46 a 60 anos     x           n.n    (4)
#Acima de 60 anos    x           n.n    (5)

listaIdade = [0, 0, 0, 0, 0,]
listaPct = [0, 0, 0, 0, 0,]

faixa1 = 0
faixa2 = 0
faixa3 = 0
faixa4 = 0
faixa5 = 0

for i in range(15):
    idade = int(input('Digite a idade: '))
    if idade == 0:
        print ('Digite uma idade maior que zero!')
    else:
        if idade <= 15:
            faixa1 += 1
            listaIdade[0] = faixa1
        elif idade >= 16 and idade <= 30:
            faixa2 += 1
            listaIdade[1] = faixa2
        elif idade >= 31 and idade <= 45:
            faixa3 += 1
            listaIdade[2] = faixa3
        elif idade >= 46 and idade <= 60:
            faixa4 += 1
            listaIdade[3] = faixa4
        elif idade > 60:
            faixa5 += 1
            listaIdade[4] = faixa5
i += 1
listaPct[0] = int((100 * faixa1) / 15)
listaPct[1] = int((100 * faixa2) / 15)
listaPct[2] = int((100 * faixa3) / 15)
listaPct[3] = int((100 * faixa4) / 15)
listaPct[4] = int((100 * faixa5) / 15)
print()
print()
print ('FAIXA ETÁRIA',  '{0:>16}'.format('TOTAL'),'{0:>17}'.format('%'))
print ('Até 15 anos     ','{0:>10}'.format(listaIdade[0]),'{0:>20}{0:.2f}'.format(listaPct[0]))
print ('De 16 a 30 anos ','{0:>10}'.format(listaIdade[1]),'{0:>20}'.format(listaPct[1]))
print ('De 31 a 45 anos ','{0:>10}'.format(listaIdade[2]),'{0:>20}'.format(listaPct[2]))
print ('De 46 a 60 anos ','{0:>10}'.format(listaIdade[3]),'{0:>20}'.format(listaPct[3]))
print ('Acima de 60 anos','{0:>10}'.format(listaIdade[4]),'{0:>20}'.format(listaPct[4]))


