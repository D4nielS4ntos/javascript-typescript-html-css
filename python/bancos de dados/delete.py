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


def deletar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print('registro removido')


id = input('Digite o id a ser excluído: ')

os.system('cls')
vcon = ConexaoBanco()
vsql = 'DELETE FROM tb_contatos WHERE ID_CONTATO = "'+id+'"'

print(vsql)
deletar(vcon, vsql)
vcon.close()
