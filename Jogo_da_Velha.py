def jogada(jogo, tabela):
    tenta = input("Digite sua jogada: ")
    try:
        tenta = int(tenta)
        if type(jogo[tabela[tenta][0]][tabela[tenta][1]]) == type(1):
            return tenta
        print("Digite uma jogada válida!")
        return jogada(jogo, tabela)
    
    except ValueError:
        print("Digite uma jogada válida!")
        return jogada(jogo, tabela)

def ha_movimentos(jogo, jogador):
    acabou = True
    for i in range(3):
        for j in range(3):
            if type(jogo[i][j]) == type(1):
                acabou = False
                break
        if not acabou:
            break
    
    if not acabou:
        if jogo[0][0] == jogo[0][1] and jogo[0][1] == jogo[0][2]:
            return f"Jogador {jogador} ganhou!"
        elif jogo[1][0] == jogo[1][1] and jogo[1][1] == jogo[1][2]:
            return f"Jogador {jogador} ganhou!"
        elif jogo[2][0] == jogo[2][1] and jogo[2][1] == jogo[2][2]:
            return f"Jogador {jogador} ganhou!"
        elif jogo[0][0] == jogo[1][0] and jogo[1][0] == jogo[2][0]:
            return f"Jogador {jogador} ganhou!"
        elif jogo[0][1] == jogo[1][1] and jogo[1][1] == jogo[2][1]:
            return f"Jogador {jogador} ganhou!"
        elif jogo[0][2] == jogo[1][2] and jogo[1][2] == jogo[2][2]:
            return f"Jogador {jogador} ganhou!"
        elif jogo[0][0] == jogo[1][1] and jogo[1][1] == jogo[2][2]:
            return f"Jogador {jogador} ganhou!"
        elif jogo[0][2] == jogo[1][1] and jogo[1][1] == jogo[2][0]:
            return f"Jogador {jogador} ganhou!"
        else:
            return "continuar"
    else:
        return "Empate!"

opcao = 'y'
jogador = "X"

while True:
    if opcao == "n":
        break
    else:
        jogo_da_velha = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        tabela_cod = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2]}
        acao = "continuar"

        while acao == "continuar":
            print()
            print(f"Vez de {jogador}")
            for i in range(3):
                print(*jogo_da_velha[i], sep=" | ")
                if i != 2:
                    print("---------")

            print()
            movimento = jogada(jogo_da_velha, tabela_cod)
            jogo_da_velha[tabela_cod[movimento][0]][tabela_cod[movimento][1]] = jogador

            acao = ha_movimentos(jogo_da_velha, jogador)

            if jogador == "X":
                jogador = "O"
            else:
                jogador = "X"
        print(acao)

    opcao = input("Deseja jogar novamente(y/n): ").lower()
    while opcao != "y" and opcao != "n":
        print("Ação Inválida")
        opcao = input("Deseja jogar novamente(y/n): ").lower()
