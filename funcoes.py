import random

def rolar_dados(numero_dados):
    lista = []
    for valor in range(numero_dados):
        valor = random.randint(1,6)
        lista.append(valor)

    return lista

def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    lista_restantes = []
    for i in range(len(dados_rolados)):
        if i == dado_para_guardar:
            continue
        lista_restantes.append(dados_rolados[i])
    estoque_novo = dados_no_estoque
    estoque_novo.append(dados_rolados[dado_para_guardar])

    return [lista_restantes,estoque_novo]
    
