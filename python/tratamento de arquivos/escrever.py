with open('texto.txt', 'at') as documento:
    texto = 'hello world \n'
    documento.write(texto)
    documento.close()

documento = open('texto.txt', 'r')
print(documento.read())
documento.close()
