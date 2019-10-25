#Faça um programa em PYTHON que leia um número e imprima o seu fatorial.
#Lembrando que:
#𝑛!=𝑛∗(𝑛−1)∗(𝑛−2)∗...∗1

#𝐸𝑥𝑒𝑚𝑝𝑙𝑜:6!=6∗5∗4∗3∗2∗1
#6!=720

#Lembrando ainda que: 0!=1

valor = int(input('Digite um valor: '))
n = valor
#############################################
if (valor == 1) or (valor == 0):
    print (n,'!=''1')
else:
    if valor < 0:
        print ('Não existe fatorial')
##############################################
    else:
        fatorial = valor
    while valor > 1:
        valor -= 1
        fatorial = fatorial * valor
##############################################
    print (n,'!=',fatorial)