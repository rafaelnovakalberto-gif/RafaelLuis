from funcoes import *
 
cartela = {
    'regra_simples': {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1},
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1,
    }
}
 
simples = ["1", "2", "3", "4", "5", "6"]
avancadas = ["sem_combinacao", "quadra", "full_house", "sequencia_baixa", "sequencia_alta", "cinco_iguais"]
 
MSG_OPCAO = "Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:"
MSG_GUARDAR = "Digite o índice do dado a ser guardado (0 a 4):"
MSG_REMOVER = "Digite o índice do dado a ser removido (0 a 4):"
MSG_COMB = "Digite a combinação desejada:"
 
def mostra_estado(rolados, guardados):
    print(f"Dados rolados: {rolados}")
    print(f"Dados guardados: {guardados}")
    print(MSG_OPCAO)
 
imprime_cartela(cartela)
 
for rodada in range(12):
    rolados = rolar_dados(5)
    guardados = []
    rerrolagens = 0
    fim_rodada = False
 
    mostra_estado(rolados, guardados)
 
    while not fim_rodada:
        opcao = input()
 
        if opcao == "1":
            print(MSG_GUARDAR)
            i = int(input())
            r = guardar_dado(rolados, guardados, i)
            rolados, guardados = r[0], r[1]
            mostra_estado(rolados, guardados)
 
        elif opcao == "2":
            print(MSG_REMOVER)
            i = int(input())
            r = remover_dado(rolados, guardados, i)
            rolados, guardados = r[0], r[1]
            mostra_estado(rolados, guardados)
 
        elif opcao == "3":
            if rerrolagens >= 2:
                print("Você já usou todas as rerrolagens.")
            else:
                rolados = rolar_dados(len(rolados))
                rerrolagens += 1
            mostra_estado(rolados, guardados)
 
        elif opcao == "4":
            imprime_cartela(cartela)
            mostra_estado(rolados, guardados)
 
        elif opcao == "0":
            todos = rolados + guardados
            print(MSG_COMB)
            while not fim_rodada:
                comb = input()
                if comb in simples:
                    if cartela['regra_simples'][int(comb)] != -1:
                        print("Essa combinação já foi utilizada.")
                    else:
                        cartela = faz_jogada(todos, comb, cartela)
                        fim_rodada = True
                elif comb in avancadas:
                    if cartela['regra_avancada'][comb] != -1:
                        print("Essa combinação já foi utilizada.")
                    else:
                        pts = calcula_pontos_regra_avancada(todos)
                        cartela['regra_avancada'][comb] = pts[comb]
                        fim_rodada = True
                else:
                    print("Combinação inválida. Tente novamente.")
 
        else:
            print("Opção inválida. Tente novamente.")
 
pontuacao = 0
soma_simples = 0
for v in cartela['regra_simples'].values():
    if v != -1:
        soma_simples += v
        pontuacao += v
if soma_simples >= 63:
    pontuacao += 35
for v in cartela['regra_avancada'].values():
    if v != -1:
        pontuacao += v
 
imprime_cartela(cartela)
print(f"Pontuação total: {pontuacao}") 