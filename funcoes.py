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

def calcula_pontos_sequencia_alta (entrada):
    dicionario_aparicoes = {
    1:0,
    2:0,
    3:0,
    4:0,
    5:0,
    6:0,
}
    for numero in entrada:
        dicionario_aparicoes[numero] += 1
    
    for i in range(2):
        if dicionario_aparicoes[1+i] >= 1 and dicionario_aparicoes[2+i] >= 1 and dicionario_aparicoes[3+i] >= 1 and dicionario_aparicoes[4+i]>= 1 and dicionario_aparicoes[5+i]>= 1:
            return 30 
    
    return 0


def calcula_pontos_full_house(dados):
    contagem = {}
    for valor in dados:
        if valor not in contagem:
            contagem[valor] = 0
        contagem[valor] += 1

    valores = list(contagem.values())
                   
    if 3 in valores and 2 in valores:
        soma = 0
        for valor in dados:
            soma += valor
        return soma

    return 0

def calcula_pontos_quadra(dados):
    contagem = {}

    for valor in dados:
        if valor not in contagem:
            contagem[valor] = 0
        contagem[valor] += 1

    for quantidade in contagem.values():
        if quantidade >= 4:
            soma = 0
            for valor in dados:
                soma += valor
            return soma

    return 0

def calcula_pontos_quina(dados):
    contagem = {}

    for valor in dados:
        if valor not in contagem:
            contagem[valor] = 0
        contagem[valor] += 1

    for quantidade in contagem.values():
        if quantidade >= 5:
            return 50
    
    return 0

def calcula_pontos_regra_avancada(dados):
    pontuacoes = {
        "cinco_iguais": calcula_pontos_quina(dados),
        "full_house": calcula_pontos_full_house(dados),
        "quadra": calcula_pontos_quadra(dados),
        "sem_combinacao": calcula_pontos_soma(dados),
        "sequencia_alta": calcula_pontos_sequencia_alta(dados),
        "sequencia_baixa": calcula_pontos_sequencia_baixa(dados)
    }

    return pontuacoes

def faz_jogada(dados, categoria, cartela_de_pontos):
    pontos_simples = calcula_pontos_regra_simples(dados)
    pontos_avancados = calcula_pontos_regra_avancada(dados)
    
    if categoria == "1" or categoria == "2" or categoria == "3" or categoria == "4" or categoria == "5" or categoria == "6":
        categoria_num = int(categoria)
        cartela_de_pontos["regra_simples"][categoria_num] = pontos_simples[categoria_num]
    else:
        cartela_de_pontos["regra_avancada"][categoria] = pontos_avancados[categoria]

    return cartela_de_pontos