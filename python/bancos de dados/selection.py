import os

import sqlite3
from sqlite3 import Error


def ConexaoBanco():
    caminho = '''C:\\Users\\Danie\\OneDrive\\Área de Trabalho\\Programação\\Geral\\Exercícios\\python\\bancos de dados\\BANCO\\banco_teste'''
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con


def consultar(conexao, sql):
    c = conexao.cursor()
    c.execute(sql)
    resultado = c.fetchall()
    print('registro alterado')
    return resultado


# nome = input('Digite o seu nome: ')
# telefone = input('Digite o seu telefone: ')
# email = input('Digite o seu email: ')
# id = input('Digite o id a ser alterado: ')

os.system('cls')
vcon = ConexaoBanco()
vsql = 'SELECT * FROM tb_contatos'
print(vsql)
dados = consultar(vcon, vsql)
for dado in dados:
    print(dado)
vcon.close()
