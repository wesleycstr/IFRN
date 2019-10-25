mascara = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for numero in mascara:
    if numero == 1: continue
else:
   n = (mascara.index(numero))
validador = []
for i in range (n,33):
    validador.append(mascara[i])
if 1 in validador:
    print ('Não é válida!')
else:
    print ('Válida!')

