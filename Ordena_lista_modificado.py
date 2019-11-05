import sys
import datetime

ordenar = False

try:
    arquivo = open('listaoriginal.txt', 'r')
    linha   = True
    valores = []
    while linha:
        linha = arquivo.readline()[:-1]
        valores.append(linha)
    arquivo.close()
    valores.pop()
    valores = [int(j) for j in valores]
    ordenar = True
 
except FileNotFoundError:
   print('Arquivo Inexistente: LISTAORIGINAL.TXT')
except:
   print('Houve um Erro...{0}'.format(sys.exc_info()[0]))
print (valores)
#------------------------------------------------------------------------
print('')
print('------------------------------------------------------------------')
print('Ordenando a Lista Gerada: ')
print('')
horaInicial = datetime.datetime.now()
print('Ordenação Iniciada às...: {0}'.format(horaInicial))

#========================================================================
# In�cio do algoritmo de ordena��o
qt_iteracoes  = 0
flag = 0
while flag == 0:
   flag = 1
   for i in range(len(valores)-1):
      if valores[i] > valores[i+1]:
         valores[i], valores[i+1] = valores[i+1], valores[i]
         qt_iteracoes += 1
         flag = 0     
print(valores)

# Final do algoritmo de ordena��o
#========================================================================

print('')
horaFinal= datetime.datetime.now()
print('Ordenação Finalizada às.: {0}'.format(horaFinal))
print('')

tempoGasto = horaFinal - horaInicial
print('Tempo de Ordenação......: {0}'.format(tempoGasto))
print('')
print('Quantidade de Iterações.: {0}'.format(qt_iteracoes))
print('------------------------------------------------------------------')
#------------------------------------------------------------------------


#------------------------------------------------------------------------
# Salvando a lista ordenada em arquivo
arquivo = open('listaordenada.txt','w')
for valor in valores:
   arquivo.write('{0}\n'.format(valor))
arquivo.close()
