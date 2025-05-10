import json

print('---------------------------------')
with open('jogo.json') as jogo:
    infos = json.load(jogo)

print(infos)

for info in infos.keys():
    print(info)
for info in infos.values():
    print(info)

infos['numero_testes'] += 1
pontuacao_maxima = int(input('Digite a pontuação: '))
if pontuacao_maxima > infos['pontuacao_maxima']: infos['pontuacao_maxima'] = pontuacao_maxima

print(infos)
infos = json.dumps(infos, indent=4)
print(infos)


json_jogo = open('jogo.json', 'wt')
json_jogo.write(infos)
json_jogo.close()
print('---------------------------------')
