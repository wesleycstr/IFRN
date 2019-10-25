while True:
   try:
      ip_1 = input('Digite o primeiro número IP no formato xxx.xxx.xxx.xxx: ')
      ip_1_dec = ip_1.split('.')
      ip_1_bin = []
      for numero in ip_1_dec:
         ip_bin = '{0:b}'.format(int(numero))
         ip_1_bin.append(ip_bin.zfill(8))
      ip_1_bin_32 = ip_1_bin[0]+ip_1_bin[1]+ip_1_bin[2]+ip_1_bin[3]
   except:
      print ('Erro! Digite o IP no formato solicitado.')
      continue
   if len (ip_1_dec) != 4 or len (ip_1_bin_32) != 32:
      print (len(ip_1_dec))
      print (ip_1_dec)
      print (ip_1_bin_32)
      print (len(ip_1_bin_32))
      print('Erro! Digite o IP no formato solicitado.')
   else: break
while True:
   try:
      ip_2 = input('Digite o segundo número IP no formato xxx.xxx.xxx.xxx: ')
      ip_2_dec = ip_2.split('.')
      ip_2_bin = []
      for numero in ip_2_dec:
         ip_bin = '{0:b}'.format(int(numero))
         ip_2_bin.append(ip_bin.zfill(8))
      ip_2_bin_32 = ip_2_bin[0]+ip_1_bin[1]+ip_1_bin[2]+ip_1_bin[3]
   except:
      print ('Erro! Digite o IP no formato solicitado.')
      continue
   if len (ip_2_dec) != 4 or len (ip_2_bin_32) != 32:
      print (len(ip_2_dec))
      print (ip_2_dec)
      print (ip_2_bin_32)
      print (len(ip_2_bin_32))
      print('Erro! Digite o IP no formato solicitado.')
   else: break
