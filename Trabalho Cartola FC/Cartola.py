import json, sys

############################################################################################################
dados_cartola = open('C:/Users/administrator/Desktop/Trabalho Cartola FC/dados_cartola.json', 'r', encoding='utf8', errors='ignore')
cartola_json = json.loads(dados_cartola.read())

clubes = cartola_json['clubes']
atletas = cartola_json['atletas']

#Separando os dados em listas:
goleiros = list()
goleiros_pontos = list()
goleiros_clubes = list()
laterais = list()
laterais_pontos = list()
laterais_clubes = list()
zagueiros = list()
zagueiros_pontos = list()
zagueiros_clubes = list()
meias = list()
meias_pontos = list()
meias_clubes = list()
atacantes = list()
atacantes_pontos = list()
atacantes_clubes = list()
tecnicos = list()
tecnicos_pontos = list()
tecnicos_clubes = list()

for i in atletas:
        if i['posicao_id']== 1:
                goleiros.append(i['apelido'])
                id_clube = str(i['clube_id'])
                goleiros_clubes.append(clubes[id_clube]['nome'])
                goleiros_pontos.append(round(i['media_num']*i['jogos_num'],2))
        if i['posicao_id']== 2:
                laterais.append(i['apelido'])
                id_clube = str(i['clube_id'])
                laterais_clubes.append(clubes[id_clube]['nome'])
                laterais_pontos.append(round(i['media_num']*i['jogos_num'],2))
        if i['posicao_id']== 3:
                zagueiros.append(i['apelido'])
                id_clube = str(i['clube_id'])
                zagueiros_clubes.append(clubes[id_clube]['nome'])
                zagueiros_pontos.append(round(i['media_num']*i['jogos_num'],2))
        if i['posicao_id']== 4:
                meias.append(i['apelido'])
                id_clube = str(i['clube_id'])
                meias_clubes.append(clubes[id_clube]['nome'])
                meias_pontos.append(round(i['media_num']*i['jogos_num'],2))
        if i['posicao_id']== 5:
                atacantes.append(i['apelido'])
                id_clube = str(i['clube_id'])
                atacantes_clubes.append(clubes[id_clube]['nome'])
                atacantes_pontos.append(round(i['media_num']*i['jogos_num'],2))
        if i['posicao_id']== 6:
                tecnicos.append(i['apelido'])
                id_clube = str(i['clube_id'])
                tecnicos_clubes.append(clubes[id_clube]['nome'])
                tecnicos_pontos.append(round(i['media_num']*i['jogos_num'],2))

#Separando os 05 melhores de cada posição:
melhores_goleiros = list()
pontos_goleiros = list()
times_goleiros = list()
melhores_laterais = list()
pontos_laterais = list()
times_laterais = list()
melhores_zagueiros = list()
pontos_zagueiros = list()
times_zagueiros = list()
melhores_atacantes = list()
pontos_atacantes = list()
times_atacantes = list()
melhores_meias = list()
pontos_meias = list()
times_meias = list()
melhores_tecnicos = list()
pontos_tecnicos = list()
times_tecnicos = list()


for i in range(5):
        pontos_goleiros.append(max(goleiros_pontos))
        melhores_goleiros.append(goleiros[goleiros_pontos.index(max(goleiros_pontos))])
        times_goleiros.append(goleiros_clubes[goleiros_pontos.index(max(goleiros_pontos))])
        goleiros_pontos.remove(max(goleiros_pontos))

        pontos_zagueiros.append(max(zagueiros_pontos))
        melhores_zagueiros.append(zagueiros[zagueiros_pontos.index(max(zagueiros_pontos))])
        times_zagueiros.append(zagueiros_clubes[zagueiros_pontos.index(max(zagueiros_pontos))])
        zagueiros_pontos.remove(max(zagueiros_pontos))

        pontos_laterais.append(max(laterais_pontos))
        melhores_laterais.append(laterais[laterais_pontos.index(max(laterais_pontos))])
        times_laterais.append(laterais_clubes[laterais_pontos.index(max(laterais_pontos))])
        laterais_pontos.remove(max(laterais_pontos))

        pontos_meias.append(max(meias_pontos))
        melhores_meias.append(meias[meias_pontos.index(max(meias_pontos))])
        times_meias.append(meias_clubes[meias_pontos.index(max(meias_pontos))])
        meias_pontos.remove(max(meias_pontos))

        pontos_atacantes.append(max(atacantes_pontos))
        melhores_atacantes.append(atacantes[atacantes_pontos.index(max(atacantes_pontos))])
        times_atacantes.append(atacantes_clubes[atacantes_pontos.index(max(atacantes_pontos))])
        atacantes_pontos.remove(max(atacantes_pontos))

        pontos_tecnicos.append(max(tecnicos_pontos))
        melhores_tecnicos.append(tecnicos[tecnicos_pontos.index(max(tecnicos_pontos))])
        times_tecnicos.append(tecnicos_clubes[tecnicos_pontos.index(max(tecnicos_pontos))])
        tecnicos_pontos.remove(max(tecnicos_pontos))

print (melhores_goleiros)
print (pontos_goleiros)
print (times_goleiros)
print()
print (melhores_laterais)
print (pontos_laterais)
print (times_laterais)
print()
print (melhores_atacantes)
print (pontos_atacantes)
print (times_atacantes)
print()
print (melhores_zagueiros)
print (pontos_zagueiros)
print (times_zagueiros)
print()
print (melhores_meias)
print (pontos_meias)
print (times_meias)
print()
print (melhores_tecnicos)
print (pontos_tecnicos)
print (times_tecnicos)


###################################################################################################################
'''
while true:
        try:
                print ('Escolha o esquema tático desejado:')
                print('1: 5-4-1')
                print('2: 5-3-2')
                print('3: 4-5-1')
                print('4: 4-4-2')
                print('5: 4-3-3')
                print('6: 5-3-2')
                print('7: 3-4-3')
                print()
                opção = input('>>> ')
                if opção == 1:
                        for i in range
                if opção == 2:
                if opção == 3:
                if opção == 4:
                if opção == 5:
                if opção == 6:
                if opção == 7:
                else: continue
        except:
                continue
'''