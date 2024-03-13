def cria_tabuleiro():
    # Inicializa o tabuleiro 3x3 com zeros
    return [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def exibe_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        for valor in linha:
            if valor == 0:
                print("__", end=" ")
            elif valor == 1:
                print("X", end=" ")
            else:
                print("O", end=" ")
        print()

def verifica_vitoria(tabuleiro):
    # Implemente a lógica para verificar vitória
    # (linhas, colunas e diagonais)
    # Retorne True se alguém ganhar, senão False
    pass

def main():
    tabuleiro = cria_tabuleiro()
    jogada = 0

    while True:
        exibe_tabuleiro(tabuleiro)
        jogador = (jogada % 2) + 1

        try:
            linha = int(input(f"Jogador {jogador}, escolha a linha (1, 2 ou 3): ")) - 1
            coluna = int(input(f"Jogador {jogador}, escolha a coluna (1, 2 ou 3): ")) - 1

            if tabuleiro[linha][coluna] == 0:
                tabuleiro[linha][coluna] = jogador
                jogada += 1
                if verifica_vitoria(tabuleiro):
                    print(f"Jogador {jogador} venceu!")
                    break
            else:
                print("Essa posição já está ocupada. Tente novamente.")
                jogada -= 1

        except ValueError:
            print("Entrada inválida. Digite um número de 1 a 3.")

    print("Fim do Jogo!")

if __name__ == "__main__":
    main()
