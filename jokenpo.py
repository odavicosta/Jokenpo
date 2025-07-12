from random import randint
import time

print("Suas opções:\n[0] Pedra\n[1] Papel\n[2] Tesoura")
jogada = int(input("Qual a sua jogada? "))

if jogada == 0 or jogada == 1 or jogada == 2:
    opcoes = ["Pedra", "Papel", "Tesoura"]

    jogada_pc = randint(0, 2)
    escolha_pc = opcoes[jogada_pc]

    escolha_jogador = opcoes[jogada]

    print("JO")
    time.sleep(1)
    print("KEN")
    time.sleep(1)
    print("PO")
    time.sleep(0.5)
    print("-=" * 13)
    print(f"O computador jogou {escolha_pc}.")
    print(f"O jogador jogou {escolha_jogador}.")
    print("-=" * 13)
    if escolha_jogador == escolha_pc:
        print("EMPATE!")
    elif jogada_pc == 0:
        if jogada == 1:
            print("JOGADOR VENCE!")
        elif jogada == 2:
            print("COMPUTADOR VENCE!")
    elif jogada_pc == 1:
        if jogada == 2:
            print("JOGADOR VENCE!")
        elif jogada == 0:
            print("COMPUTADOR VENCE!")
    elif jogada_pc == 2:
        if jogada == 0:
            print("JOGADOR VENCE!")
        elif jogada == 1:
            print("COMPUTADOR VENCE!")

else:
    print("Jogada inválida!")
