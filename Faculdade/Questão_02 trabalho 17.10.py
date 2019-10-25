import sys

while True:
    while True:
        while True:
            try:
                mascara = input('Digite uma máscara de rede no formato xxx.xxx.xxx.xxx: ')

                mascara_dec = mascara.split('.')

                mascara_bin=[]
                for numero in mascara_dec:
                    numero_bin = '{0:b}'.format(int(numero))
                    mascara_bin.append(numero_bin.zfill(8))
                mascara_bin_32 = mascara_bin[0]+mascara_bin[1]+mascara_bin[2]+mascara_bin[3]
                break
            except:
                print ('Erro!')
                continue
    
        if len (mascara_dec) > 4 or len (mascara_bin) > 32:
            print ('O número de caracteres digitados excedeu o limite permitido!')
            continue
        else: break

    #Separando os 32 bits da máscara em uma lista:
    lista_masc_bin_32 = []
    for numero in range (len(mascara_bin_32)):
        lista_masc_bin_32.append(mascara_bin_32[numero])

    #Validação da máscara:
    validador = []
    for i in range (lista_masc_bin_32.count('1')):
        validador.append(lista_masc_bin_32[i])
    if '0' in validador:
        print ('Esta não é uma máscara válida!')
        continue
    else: break


