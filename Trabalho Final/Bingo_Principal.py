import lib_cartelas # Biblioteca para gerar e imprimir cartelas
import lib_arquivos # Biblioteca para salvar e ler arquivos
import random, copy, sys

cartelas_geradas = {}

while True:
   print('1 - Gerar Cartelas')
   print('2 – Imprimir Cartela')
   print('3 – Salvar Cartelas')
   print('4 – Ler Cartelas')
   print('5 – Sortear Números (Prova Final)')
   print('0 – Sair do Programa')
   print('-------------------------')

   try:
      opcao = int(input('Escolha uma opção: '))
   except ValueError:
      print('\nValor Informado Inválido...')
      continue
   except:
      print('\nErro Não Conhecido...')
      continue
   else:
      if (opcao == 1): # Gerar Cartelas
         while True:
            try:
               qtCartelas = int(input('Informe a quantidade de cartelas a serem geradas: '))
            except:
               print('Valor Informado Inválido...')
               continue
            else:
               if (qtCartelas <= 0) or (qtCartelas > 10000): continue
               cartelas_geradas = {} # Limpando as Cartelas já geradas
               cartelas_geradas = lib_cartelas.gerar_cartelas(qtCartelas)
               print('\nCartelas Geradas com Sucesso!!!\n\n')
               break
      elif (opcao == 2): # Imprimir Cartelas
         if (len(cartelas_geradas) == 0):
            print('Nao Há Cartelas a Serem Impressas\n\n')
         else:
            while True:
               try:
                  numCartela = int(input('\nInforme o número da Cartela a ser Impressa: '))
               except:
                  print('Valor Informado Inválido...\n\n')
                  continue
               else:
                  if numCartela in cartelas_geradas.keys():
                     cartela_imprimir = cartelas_geradas[numCartela]
                     print(lib_cartelas.imprime_cartela(numCartela, cartela_imprimir))
                  else:
                     print('Não Há Cartela com o Número Informado\n\n')
                  break
      elif (opcao == 3): # Salvar Cartelas em arquivo
         if (lib_arquivos.salvar_cartelas(cartelas_geradas,'cartelas.txt')):
            print('\nCartelas Salvas com Sucesso!!!')
            print('\nArquivo: CARTELAS.TXT\n\n')
         else:
            print('\nErro no Salvamento das Cartelas!!!\n\n')
      elif (opcao == 4): # Ler Cartelas de arquivo
         try:
            cartelas_geradas = {}  # Limpando as Cartelas já geradas
            cartelas_geradas = lib_arquivos.ler_cartelas('cartelas.txt')
            print('\n\n')
         except:
            print('Erro na Leitura do Arquivo...\n\n')

######################################################################################################################
      elif (opcao == 5):  # Sortear Números
         cartelas_cópia = copy.deepcopy(cartelas_geradas)

         #Sorteando os primeiros 24 números:
         num_sorteado = []
         num_gerado = ''
         while len (num_sorteado) != 24:
            num_gerado = (random.randint(1,75))
            if num_gerado not in num_sorteado:
               num_sorteado.append(num_gerado)
         print(f'Foram sorteados inicialmente estes 24 números:\n',num_sorteado)

         #Gerando uma lista de chaves:
         chaves = []
         for k in cartelas_cópia:
            chaves.append(k)
         
         #Gerando uma lista de cartelas:
         cartelas = []
         for v in cartelas_cópia.values():
            v=v[0]+v[1]+v[2]+v[3]+v[4]
            cartelas.append(v)
         
         #Verificando os números sorteados em cada cartela
         for i in range (qtCartelas):
            for j in (num_sorteado):
               if j in cartelas[i]:
                     cartelas[i].remove(j)
               else:
                     continue
         
         #Prosseguindo com o subprograma sorteio:
         qt_num = 24
         while len (num_sorteado) != 75:
            condição = ''
            while True:
               print()
               print('Escolha a opção desejada:')
               print ('1 - Sortear mais um número')
               print (f'2 - Ver as {qtCartelas} cartelas geradas')
               print ('3 - Ver os números restantes em cada cartela')
               print ('4 - Ver a quantidade de números restantes em cada cartela')
               print ('5 - Ver todos os números sorteados')
               print ('6 - Encerrar o programa')
               condição = input('>>> ').upper()
               if condição == '1':
                     break
               elif condição == '2':
                     print (f'Foram geradas essas {qtCartelas} cartelas:\n',cartelas_cópia)
                     continue
               elif condição == '3':
                     print (f'Os números restantes em cada cartela são:\n',cartelas)
                     continue

               elif condição == '4':
                     for i in range (len(cartelas)):
                        if cartelas[i]==[f'{chaves[i]}-vencedora']:
                           print ('-'*40)
                           print (f'Cartela {chaves[i]}-Vencedora')
                           print ('-'*40)
                        else:
                           print (f'Quantidade de números restantes para a cartela {chaves[i]}: ',len(cartelas[i]))

               elif condição == '5':
                     print (f'Foram sorteados {qt_num} números:\n',num_sorteado)
                     continue
               elif condição == '6':
                  sys.exit()
               else:
                     continue


            while True:
               num_gerado = (random.randint(1,75))
               if num_gerado not in num_sorteado:
                        num_sorteado.append(num_gerado)
                        qt_num += 1
                        print()
                        print(f'Número sorteado: |{num_gerado}|')
                        print(f'Quantidade de números sorteados: {qt_num}')
         #               print (cartelas_copia)
                        break
               else:
                     continue
            
            for i in range (qtCartelas):
               if num_gerado in cartelas[i]:
                     cartelas[i].remove(num_gerado)

            lista_qtd = []
            for i in range (qtCartelas):
               lista_qtd.append(len(cartelas[i]))
            menor = min(lista_qtd)
            lista_indice = []
            for i in range (len(lista_qtd)):
               if lista_qtd[i] == menor:
                     lista_indice.append(lista_qtd.index(lista_qtd[i]))
                     lista_qtd[i] = ''
            print ('Cartelas mais próximas de ganhar: ',end='')
            for i in lista_indice:
               print (chaves[i], end=' ')
            
            print('\nQuantidade de números restantes nestas cartelas: ',menor)
            
            for i in range (qtCartelas):
               if len (cartelas[i]) == 0:
                     print()
                     print('*'*40)
                     print (f'Cartela {chaves[i]} venceu!!!')
                     print('*'*40)
                     print()
                     cartelas[i].append(f'{chaves[i]}-vencedora')

######################################################################################################################
      elif (opcao == 0): # Sair do Programa
         break
      else:
         print('\nOpção Não Disponível...\n\n')