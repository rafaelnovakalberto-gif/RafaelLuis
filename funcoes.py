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
    
def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    novo_estoque = []
    for i in range(len(dados_no_estoque)):

        if i == dado_para_remover:
            dados_rolados.append(dados_no_estoque[i])
            continue
        novo_estoque.append(dados_no_estoque[i])
    
    return [dados_rolados,novo_estoque]

def calcula_pontos_regra_simples(dados_rolados):
    saida = {
        1:0,
        2:0,
        3:0,
        4:0,
        5:0,
        6:0,
    }
    for valor in dados_rolados:

        saida[valor] += valor
    
    return saida
def calcula_pontos_soma(entrada):
    soma = 0     
    for valor in entrada:
        soma += valor 
    return soma


def calcula_pontos_sequencia_baixa(dados_estoque):
    dicionario_aparicoes = {
        1:0,
        2:0,
        3:0,
        4:0,
        5:0,
        6:0,
    }

    for valor in dados_estoque:
        dicionario_aparicoes[valor] += 1
    
    if dicionario_aparicoes[1] >= 1 and dicionario_aparicoes[2] >= 1 and dicionario_aparicoes[3] >= 1 and dicionario_aparicoes[4] >= 1:
        return 15
    if dicionario_aparicoes[2] >= 1 and dicionario_aparicoes[3] >= 1 and dicionario_aparicoes[4] >= 1 and dicionario_aparicoes[5] >= 1:
        return 15
    if dicionario_aparicoes[3] >= 1 and dicionario_aparicoes[4] >= 1 and dicionario_aparicoes[5] >= 1 and dicionario_aparicoes[6] >= 1:
        return 15        
    return 0 



    