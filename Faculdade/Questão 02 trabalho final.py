import sys

while True:
    while True:
        while True:
            try:
                print ()
                #Validação dos caracteres digitados
                mascara = input('Digite uma máscara de rede no formato xxx.xxx.xxx.xxx: ')

                mascara_dec = mascara.split('.')

                mascara_bin=[]
                for numero in mascara_dec:
                    numero_bin = '{0:b}'.format(int(numero))
                    mascara_bin.append(numero_bin.zfill(8))
                mascara_bin_32 = mascara_bin[0]+mascara_bin[1]+mascara_bin[2]+mascara_bin[3]
                break
            except:
                print ('Erro! Digite a máscara de rede no formato solicitado utilizando números e separando por ponto.')
                continue
    
        if len (mascara_dec) > 4 or len (mascara_bin) > 32:
            print ('Erro! Esta não é uma máscara válida.')
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
        print ('Erro! Esta não é uma máscara válida.')
        continue
    else: break

# Recebendo IP 1 e validando
while True:
   try:
      print ()
      ip_1 = input('Digite o primeiro número IP no formato xxx.xxx.xxx.xxx: ')
      ip_1_dec = ip_1.split('.')
      ip_1_bin = []
      for numero in ip_1_dec:
         ip_bin = '{0:b}'.format(int(numero))
         ip_1_bin.append(ip_bin.zfill(8))
      ip_1_bin_32 = ip_1_bin[0]+ip_1_bin[1]+ip_1_bin[2]+ip_1_bin[3]
   except:
      print ('Erro! Digite o IP no formato solicitado utilizando apenas números e separando por pontos.')
      continue
   if len (ip_1_dec) != 4 or len (ip_1_bin_32) != 32:
      print('Erro! O IP digitado não é valido.')
   else: break

# Recebendo IP 2 e validando
while True:
   try:
      print()
      ip_2 = input('Digite o segundo número IP no formato xxx.xxx.xxx.xxx: ')
      ip_2_dec = ip_2.split('.')
      ip_2_bin = []
      for numero in ip_2_dec:
         ip_bin = '{0:b}'.format(int(numero))
         ip_2_bin.append(ip_bin.zfill(8))
      ip_2_bin_32 = ip_2_bin[0]+ip_2_bin[1]+ip_2_bin[2]+ip_2_bin[3]
   except:
      print ('Erro! Digite o IP no formato solicitado utilizando apenas números e separando por pontos.')
      continue
   if len (ip_2_dec) != 4 or len (ip_2_bin_32) != 32:
      print('Erro! O IP digitado não é válido.')
   else: break

#Calculando o endereço de rede do IP1
endereço_da_rede_1 = []

lista_ip_1_32 = []
for i in ip_1_bin_32:
    lista_ip_1_32.append(i)


for numero in range (32):
    if lista_ip_1_32[numero]=='0' or lista_masc_bin_32[numero] == '0':
        endereço_da_rede_1.append('0')
    else: endereço_da_rede_1.append('1')

#print(lista_masc_bin_32)
#print (lista_ip_1_32)
#print (endereço_da_rede_1)

#Separando o endereço de rede em octetos
end_rede_10 = ''.join(endereço_da_rede_1[0:8])
end_rede_11 = ''.join(endereço_da_rede_1[8:16])
end_rede_12 = ''.join(endereço_da_rede_1[16:24])
end_rede_13 = ''.join(endereço_da_rede_1[24:32])

#Mostrando resultados
print('-='*40)
print ('Máscara de sub-rede:      {}'.format(mascara))
print ('Endereço do IP 1:         {}'.format(ip_1))
print ('Endereço de rede do IP 1: {}.{}.{}.{}'.format(int(end_rede_10,2), int(end_rede_11,2), int(end_rede_12,2), int(end_rede_13,2)))

#Calculando o endereço de rede do IP 2
lista_ip_2_32 = []
for i in ip_2_bin_32:
    lista_ip_2_32.append(i)

endereço_da_rede_2 = []
for numero in range (32):
    if lista_ip_2_32[numero]=='0' or lista_masc_bin_32[numero] == '0':
        endereço_da_rede_2.append('0')
    else: endereço_da_rede_2.append('1')

#print(lista_masc_bin_32)
#print (lista_ip_2_32)
#print (endereço_da_rede_1)

#Separando o endereço de rede em octetos
end_rede_20 = ''.join(endereço_da_rede_2[0:8])
end_rede_21 = ''.join(endereço_da_rede_2[8:16])
end_rede_22 = ''.join(endereço_da_rede_2[16:24])
end_rede_23 = ''.join(endereço_da_rede_2[24:32])

#Mostrando resultados
print ('Endereço do IP 2:         {}'.format(ip_2))
print ('Endereço de rede do IP 2: {}.{}.{}.{}'.format(int(end_rede_20,2), int(end_rede_21,2), int(end_rede_22,2), int(end_rede_23,2)))
print()
if end_rede_10 == end_rede_20 and end_rede_11 == end_rede_21 and end_rede_12 == end_rede_22 and end_rede_13 == end_rede_23:
    print ('Estes IPs fazem parte da mesma rede!')
else:
    print ('Estes IPs não fazem parte da mesma rede!')
print ('-='*40)