import sys

while True:
    while True:
        n_ip = input('Digite um bloco de rede no formato xxx.xxx.xxx.xxx/xx: ')
        ip_separado = n_ip.split('/')

        ip = ip_separado[0]
        cidr = ip_separado[1]

        if int(cidr) < 8 or int(cidr) > 32:
            print ('A máscara de sub-rede digitada não é válida!')
            continue
        else: break
        
    try:
        ip_dec = ip.split('.')

        ip_bin = []
        for numero in ip_dec:
            n_ip_bin = '{0:b}'.format(int(numero))
            ip_bin.append(n_ip_bin.zfill(8))
        ip_bin_32 = ip_bin[0]+ip_bin[1]+ip_bin[2]+ip_bin[3]
    except:
        print ('Erro###! Digite o IP no formato solicitado.')
        continue
    if len (ip_dec) != 4 or len (ip_bin_32) != 32:
        print('Erro! Digite o IP no formato solicitado.')
    else: break

#Transformando a notação CIDR em binário
masc_bin = []
for numero in range (int(cidr)):
    masc_bin.append('1')
while len(masc_bin) != 32:
    masc_bin.append('0')

#Convertendo a máscara para decimal:
masc_dec_0 = ''.join(masc_bin[0:8])
masc_dec_1 = ''.join(masc_bin[8:16])
masc_dec_2 = ''.join(masc_bin[16:24])
masc_dec_3 = ''.join(masc_bin[24:32])

print('A máscara de sub-rede é: {}.{}.{}.{}'.format(int(masc_dec_0,2), int(masc_dec_1,2), int(masc_dec_2,2), int(masc_dec_3,2)))

#Calculando o número de subredes
sub_redes = masc_dec_1 + masc_dec_2 + masc_dec_3
n = sub_redes.count('1')
total_sub_redes = 2 ** n

print ('O total de subredes é: {}'.format(total_sub_redes))

#Calculando o número de hosts:
n = masc_bin.count('0')
total_hosts = 2 ** n -2

print ('O total de hosts é: {}'.format(total_hosts))


#Calculando o endereço de rede
lista_ip_bin = []
for numero in range (32):
    lista_ip_bin.append (ip_bin_32[numero])
#print(lista_ip_bin)

end_rede = []
for i in range (32):
    if masc_bin[i] == '0' or lista_ip_bin [i] == '0':
        end_rede.append('0')
    else:
        end_rede.append('1')
#print (end_rede)

#Transformando o endereço de rede em octetos:
#Separando o endereço de rede em octetos
end_rede_0 = ''.join(end_rede[0:8])
end_rede_1 = ''.join(end_rede[8:16])
end_rede_2 = ''.join(end_rede[16:24])
end_rede_3 = ''.join(end_rede[24:32])

print ('O endereço da rede é: {}.{}.{}.{}'.format(int(end_rede_0,2), int(end_rede_1,2), int(end_rede_2,2), int(end_rede_3,2)))

#print (end_rede)
#print (masc_bin)

#Calculando broadcast:
broadcast = []
for i in range (32):
    if end_rede[i] == masc_bin[i]:
        broadcast.append('1')
    else:
        broadcast.append('0')

broadcast_0 = ''.join(broadcast[0:8])
broadcast_1 = ''.join(broadcast[8:16])
broadcast_2 = ''.join(broadcast[16:24])
broadcast_3 = ''.join(broadcast[24:32])

print('O endereço broadcast é: {}.{}.{}.{}'.format(int(broadcast_0,2), int(broadcast_1,2), int(broadcast_2,2), int(broadcast_3,2)))

#Calculando host mínimo:
print ('Os endereços válidos para cada subrede estão entre {}.{}.{}.{} e {}.{}.{}.{}'.format(int(end_rede_0,2), int(end_rede_1,2), int(end_rede_2,2), int(end_rede_3,2)+1,int(broadcast_0,2), int(broadcast_1,2), int(broadcast_2,2), int(broadcast_3,2)-1))
