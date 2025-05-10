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


def alterar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print('registro alterado')


nome = input('Digite o seu nome: ')
telefone = input('Digite o seu telefone: ')
email = input('Digite o seu email: ')
id = input('Digite o id a ser alterado: ')

os.system('cls')
vcon = ConexaoBanco()
vsql = 'UPDATE tb_contatos SET T_NOMECONTATO = "'+nome+'", T_TELEFONECONTATO = "'+telefone+'", T_EMAILCONTATO = "'+email+'" WHERE ID_CONTATO = "'+id+'"'

print(vsql)
alterar(vcon, vsql)
vcon.close()
