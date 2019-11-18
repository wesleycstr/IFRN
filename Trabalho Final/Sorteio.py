import random

#Sorteando 24 números:
num_sorteado = []
num_gerado = ''
while len (num_sorteado) != 24:
    num_gerado = (random.randint(1,75))
    if num_gerado not in num_sorteado:
        num_sorteado.append(num_gerado)
print('Foram sorteados estes 24 números:')
print (num_sorteado)

#Sorteando um número por vez:
qt_num = 24
while len (num_sorteado) != 75:
    condição = ''
    while True:
        print()
        print ('Digite (S) para sortear mais um número')
        condição = input('>>> ').upper()
        if condição == 'S':
            break
        else:
            continue
    while True:
        num_gerado = (random.randint(1,75))
        if num_gerado not in num_sorteado:
                num_sorteado.append(num_gerado)
                qt_num += 1
                print()
                print(f'Número sorteado: {num_gerado}')
                print(f'Quantidade de números sorteados: {qt_num}')
                break
        else:
            continue
    print (num_sorteado)
    continue
