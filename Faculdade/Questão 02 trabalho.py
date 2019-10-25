#Fazer  um  programa  em  Python  que  solicite  uma  máscara  de  rede  (a  máscara  deverá  ser informada em decimal) 
#e 2 endereços IP (em formato decimal) e informar se os 2 IPs pertencem a mesma rede.

mascara = '255.255.255.000'
mascara_bin = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0]
ip_1 = '192.168.1.61'
ip_1_bin = [1,1,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,1,1,0,1]


c = mascara_bin.count(1)
print (c)
#print (ip_1_bin)

ip_rede = []
for i in range (c):
    ip_rede.append(str(ip_1_bin[i]))

while len(ip_rede) < 32:
    ip_rede.append ('0')
print (ip_rede)
print (len(ip_rede))

octeto_0 = str(ip_rede[0]+ip_rede[1]+ip_rede[2]+ip_rede[3]+ip_rede[4]+ip_rede[5]+ip_rede[6]+ip_rede[7])
octeto_1 = str(ip_rede[8]+ip_rede[9]+ip_rede[10]+ip_rede[11]+ip_rede[12]+ip_rede[13]+ip_rede[14]+ip_rede[15])
octeto_2 = str(ip_rede[16]+ip_rede[17]+ip_rede[18]+ip_rede[19]+ip_rede[20]+ip_rede[21]+ip_rede[22]+ip_rede[23])
octeto_3 = str(ip_rede[24]+ip_rede[25]+ip_rede[26]+ip_rede[27]+ip_rede[28]+ip_rede[29]+ip_rede[30]+ip_rede[31])

print ('O endereço de rede é {}.{}.{}.{}'.format(int(octeto_0,2), int(octeto_1,2), int(octeto_2,2), int(octeto_3,2)))