import time

inicio = time.time()
for i in range(1000):
    print(i)
fim = time.time()
print(f"Tempo de execução: {fim - inicio} segundos")