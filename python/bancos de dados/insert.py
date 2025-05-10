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


def inserir(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print('registro inserido')
    except Error as ex:
        print(ex)


nome = input('Digite seu nome: ')
telefone = input('Digite seu telefone: ')
contato = input('Digite seu contato: ')

os.system('cls')
vcon = ConexaoBanco()
vsql = 'INSERT INTO tb_contatos (T_NOMECONTATO,T_TELEFONECONTATO, T_EMAILCONTATO) VALUES("'+nome+'", "'+telefone+'", "'+contato+'")'
print(vsql)

inserir(vcon, vsql)
vcon.close()
