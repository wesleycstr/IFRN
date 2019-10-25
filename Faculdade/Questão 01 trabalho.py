
while True:
    n = input('Digite uma máscara de rede: ')
    lista_n = []
    for i in n:
        if i.isdigit():
            lista_n.append(i)
#print ('Somente os digitos informados: ',lista_n)


    while len (lista_n) < 13:
        lista_n.append('0')
    print ('Digitos informados com zeros completados: ', lista_n)

    n_inteiro = str(''.join(lista_n))
    print ('Número inteiro fora da lista: ',n_inteiro)

    octeto_0 =  int(n_inteiro[0:3])
    octeto_1 = int(n_inteiro[3:6])
    octeto_2 = int(n_inteiro[6:9])
    octeto_3 = int(n_inteiro[9:12])

    print ('Confirma a máscara de rede digitada? {}.{}.{}.{}'.format(octeto_0, octeto_1, octeto_2, octeto_3))
    confirma = ''
    while confirma != 'S' and confirma != 'N':
        confirma = input('Digite S para confirmar ou N para digitar novamente: ').upper()
    if confirma == 'N': continue
    elif confirma == 'S': break

octeto_bin_0 = '{:b}'.format(octeto_0).zfill(8)
octeto_bin_1 = '{:b}'.format(octeto_1).zfill(8)
octeto_bin_2 = '{:b}'.format(octeto_2).zfill(8)
octeto_bin_3 = '{:b}'.format(octeto_3).zfill(8)
#print (octeto_bin_0,octeto_bin_1,octeto_bin_2,octeto_bin_3)
masc_bin = str(octeto_bin_0+octeto_bin_1+octeto_bin_2+octeto_bin_3)
#print (masc_bin)
lista_bin = [masc_bin]
lista_bin_2 = []
print (lista_bin)
for i in range (0,20):
    lista_bin_2.append(masc_bin[i])
print (lista_bin_2)

n_bin_inteiro = str(','.join(lista_bin_2))
#print (n_bin_inteiro)
c = n_bin_inteiro.count('1')
lista = []
print (c)
for i in range(c):
    lista.append(c[1])
print (lista_1)
if 0 in lista_1:
    print ('Esta não é uma máscara válida')
else:
    print ('Máscara válida!')