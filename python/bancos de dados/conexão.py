import os

import sqlite3
from sqlite3 import Error


def ConexaoBanco():
    caminho = '''C:\\Users\\Danie\\OneDrive\\Área de Trabalho\\Programação\\Geral\\Exercícios\\python\\bancos de dados\\BANCO\\banco_teste.db'''
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con
    

os.system('cls')
vcon = ConexaoBanco()

vcon.close()
