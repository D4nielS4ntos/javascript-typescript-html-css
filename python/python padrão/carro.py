import os


carros = []

class Carro:
    nome = ''
    pot = 0
    velMax = 0
    ligado = False
    def __init__(self, nome, pot):
        self.nome = nome
        self.pot = pot
        self.velMax = int(pot) * 2
        self.ligado = False

    def ligar(self):
        self.ligado = True
    
    def desligar(self):
        self.ligado = False

    def info(self):
        mensagem = ''
        mensagem += f'Nome........: {self.nome}\n'
        mensagem += f'Potência....: {self.pot}\n'
        mensagem += f'Vel. Máxima.: {self.velMax}\n'
        mensagem += f'Ligado......: '+('sim' if self.ligado==True else 'não')+'\n'
        print(mensagem)

def menu():
    os.system('cls') or None
    mensagem = ''
    mensagem += f'1 - Novo Carro\n'
    mensagem += f'2 - Informações do Carro\n'
    mensagem += f'3 - Excluir Carro\n'
    mensagem += f'4 - Ligar Carro\n'
    mensagem += f'5 - Desligar Carro\n'
    mensagem += f'6 - Listar Carro\n'
    mensagem += f'7 - Sair\n'
    mensagem += f'Quantidade de carros {len(carros)}\n'
    print(mensagem)
    opcao = input('Digite uma opção: ')
    return opcao
    
def novo_carro():
    os.system('cls') or None
    nome = input('Nome do carro.....:')
    potencia = input('Potência do carro.:')
    car = Carro(nome, potencia)
    carros.append(car)
    print('Novo carro')
    os.system('pause')

def info_carro():
    os.system('cls') or None
    numero = input('Informe o número do carro que deseja ver as informações: ')
    try:
        carros[int(numero)].info()
    except:
        print('Carro não existe nessa lista.')
    os.system('pause')

def excluir_carro():
    os.system('cls') or None
    numero = input('Informe o número do carro que deseja excluir as informações: ')
    try:
        del carros[int(numero)]
    except:
        print('Carro não existe nessa lista.')
    os.system('pause')

def ligar_carro():
    os.system('cls') or None
    numero = input('Informe o número do carro que deseja ligar: ')
    try:
        carros[int(numero)].ligar()
        print('Carro ligado.')
    except:
        print('Carro não existe nessa lista.')
    os.system('pause')

def desligar_carro():
    os.system('cls') or None
    numero = input('Informe o número do carro que deseja ligar: ')
    try:
        carros[int(numero)].desligar()
        print('Carro desligado.')
    except:
        print('Carro não existe nessa lista.')
    os.system('pause')

def listar_carros():
    os.system('cls') or None
    posicao = 0
    for carro in carros:
        print(f'{posicao} - {carro.nome}')
        posicao += 1
    os.system('pause')


retorno = menu()
while retorno < '7':
    if retorno == '1':
        novo_carro()
    elif retorno == '2':
        info_carro()
    elif retorno == '3':
        excluir_carro()
    elif retorno == '4':
        ligar_carro()
    elif retorno == '5':
        desligar_carro()
    elif retorno ==  '6':
        listar_carros()
    retorno = menu()
os.system('cls') or None
print('Programa finalizado')
