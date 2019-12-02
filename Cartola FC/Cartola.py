import json


dados_cartola = open('C:/Users/Usuario/Desktop/Cartola FC/dados_cartola.json', 'r', encoding='utf8', errors='ignore')
cartola_json = json.loads(dados_cartola.read())

clubes = cartola_json['clubes']
atletas = cartola_json['atletas']
posicoes = cartola_json['posicoes']
status = cartola_json['status']


print (clubes['262']['nome'])


for i in clubes:
    print(clubes[i]['nome'])

print (clubes.keys())

print (atletas)


for i in atletas:
    print (i['apelido'])

    