#Fazer um programa em Python que solicite uma máscara de rede (a máscara deverá ser informada em decimal) e:
#(a) Informar se a máscara é válida ou não;
#(b) Em sendo válida, informar qual a classe da máscara (A, B, C ou CIDR)


while True:
    mascara = input('Informe uma máscara de rede: ')
    
    m_dec = mascara.split('.')
    m_bin = []

    for i in m_dec:
        numero_bin = '{:b}'.format(int(i))
        m_bin.append(numero_bin.zfill(8))

    j = ''
    j = j.join (m_bin)
    if len (j) != 32:
        print ('Digite uma máscara de rede válida!')
        print (len(j))
        continue
    else: break
    
print (len(j))
print (m_bin)
print (j)
