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


def CriarTabela(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        print('Tabela criada')
    except Error as ex:
        print(ex)
    

os.system('cls')
vcon = ConexaoBanco()
vsql = '''CREATE TABLE tb_contatos2(
            N_IDCONTATO INTEGER PRIMATY KEY AUTOINREMENT, T_NOMECONTATO VARCHAR(30),
            T_EMAILCONTATO VARCHAR(30)
        );'''

CriarTabela(vcon, vsql)
vcon.close()
