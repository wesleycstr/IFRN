# --------------------------------------------------------------------------
# Biblioteca contendo as funções para geração e impressão
# das cartelas de bingo
# --------------------------------------------------------------------------

import random

# --------------------------------------------------------------------------
# Função para gerar dicionário com as cartelas
def gerar_cartelas(intQtCartelas):
   cartelas_retorno = {}
   contCartelas = 1
   while (contCartelas <= intQtCartelas):
      numero_cartela = random.randint(1, 10000)
      if (numero_cartela not in cartelas_retorno.keys()):
         numero_gerados_cartela = gerar_numeros_cartela()
         if (numero_gerados_cartela not in cartelas_retorno.values()):
            cartelas_retorno[numero_cartela] = numero_gerados_cartela
            contCartelas += 1
   return cartelas_retorno
# --------------------------------------------------------------------------


# --------------------------------------------------------------------------
# Função para gerar a cartela 
def gerar_numeros_cartela():
   cartela = []
   cartela.append(gera_lista( 1,15)) # Coluna Letra B
   cartela.append(gera_lista(16,30)) # Coluna Letra I
   cartela.append(gera_lista(31,45)) # Coluna Letra N
   cartela.append(gera_lista(46,60)) # Coluna Letra G
   cartela.append(gera_lista(61,75)) # Coluna Letra O
   return cartela
	
# --------------------------------------------------------------------------


# --------------------------------------------------------------------------
# Função para gerar uma lista com 5 números inteiros aleatórios 
# dentro de um intervalo especificado
def gera_lista(intValorInicial, intValorFinal):
   lista    = []
   contador = 0
   while (contador < 5):
      numero = random.randint(intValorInicial, intValorFinal)
      if numero not in lista:
         lista.append(numero)
         contador += 1
   return sorted(lista)
# --------------------------------------------------------------------------

# --------------------------------------------------------------------------
# Função para imprimir a cartela de bingo
def imprime_cartela(intNumeroCartela, lstCartela):
   cartela =           '+----+----+----+----+----+\n'
   cartela = cartela + '| Cartela: ' + str(intNumeroCartela).zfill(5) +'         | \n'
   cartela = cartela + '+----+----+----+----+----+\n'
   cartela = cartela + '|  B |  I |  N |  G |  O |\n'
   cartela = cartela + '+----+----+----+----+----+\n'
   for i in range(len(lstCartela)):
      nB = lstCartela[0][i]
      nI = lstCartela[1][i]
      nN = lstCartela[2][i]
      nG = lstCartela[3][i]
      nO = lstCartela[4][i]
      cartela = cartela + '| {0:2d} | {1:2d} | {2:2d} | {3:2d} | {4:2d} |\n'.format(nB,nI,nN,nG,nO)
      cartela = cartela + '+----+----+----+----+----+\n'
   return cartela + '\n'
# --------------------------------------------------------------------------
#Função sortear números
#Sorteando os primeiros 24 números:
def sortear_24_num():
    num_sorteado = []
    num_gerado = ''
    while len (num_sorteado) != 24:
        num_gerado = (random.randint(1,75))
        if num_gerado not in num_sorteado:
            num_sorteado.append(num_gerado)
    return num_sorteado

#Sorteando um número por vez:
def sortear_numeros(lista, cartelas):
    qt_num = 24
    while len (lista) != 75:
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
            if num_gerado not in lista:
                    lista.append(num_gerado)
                    qt_num += 1
                    print()
                    print(f'Número sorteado: {num_gerado}')
                    print(f'Quantidade de números sorteados: {qt_num}')
                    break
            else:
                continue
        print (f'Números sorteados:\n{lista}')
        print (f'Cartelas:\n{cartelas}')
        continue