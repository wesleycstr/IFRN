# --------------------------------------------------------------------------
# Biblioteca contendo as funções para salvar as cartelas em arquivo e
# ler o arquivo de cartelas quando existir
# --------------------------------------------------------------------------


# --------------------------------------------------------------------------
# Função para salvar cartelas em arquivo
def salvar_cartelas(dicCartelas, strNomeArquivo):
   retorno = False
   if (len(dicCartelas) > 0):
      arquivo = open('C:/Users/Usuario/Desktop/Trabalho Final/cartelas.txt', 'w')
      for k, v in dicCartelas.items():
         num_cartela = k
         linha = ''
         for x in range(0, 5):
            for y in range(0, 5):
               linha = linha + str(v[x][y]).zfill(2) + '#'
         linha = str(num_cartela).zfill(5) + '#' + linha[:-1] + '\n'
         arquivo.write(linha)
      arquivo.close()
      retorno = True
   return retorno
# --------------------------------------------------------------------------


# --------------------------------------------------------------------------
# Função para ler as cartelas de um arquivos
def ler_cartelas(strNomeArquivo):
   lstlinha = []
   arquivo = open('C:/Users/Usuario/Desktop/Trabalho Final/cartelas.txt', 'r')
   conteudo = arquivo.readline()
   linha = conteudo[:-1].split('#')
   lstlinha.append(linha)
   while conteudo:
      conteudo = arquivo.readline()
      linha = conteudo[:-1].split('#')
      lstlinha.append(linha)
   arquivo.close()

   lstlinha.pop()

   cartelas_retorno = {}
   for i in range(0,len(lstlinha)):
      num_cartela = int(lstlinha[i][0])
      letra_B = [int(lstlinha[i][1]),int(lstlinha[i][2]),int(lstlinha[i][3]),int(lstlinha[i][4]),int(lstlinha[i][5])]
      letra_I = [int(lstlinha[i][6]),int(lstlinha[i][7]),int(lstlinha[i][8]),int(lstlinha[i][9]),int(lstlinha[i][10])]
      letra_N = [int(lstlinha[i][11]),int(lstlinha[i][12]),int(lstlinha[i][13]),int(lstlinha[i][14]),int(lstlinha[i][15])]
      letra_G = [int(lstlinha[i][16]),int(lstlinha[i][17]),int(lstlinha[i][18]),int(lstlinha[i][19]),int(lstlinha[i][20])]
      letra_O = [int(lstlinha[i][21]),int(lstlinha[i][22]),int(lstlinha[i][23]),int(lstlinha[i][24]),int(lstlinha[i][25])]
      cartelas_retorno[num_cartela] = [letra_B,letra_I,letra_N,letra_G,letra_O]
   return cartelas_retorno
# --------------------------------------------------------------------------