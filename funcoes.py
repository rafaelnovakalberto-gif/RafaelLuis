import random

def rolar_dados(numero_dados):
    lista = []
    for valor in range(numero_dados):
        valor = random.randint(1,6)
        lista.append(valor)

    return lista