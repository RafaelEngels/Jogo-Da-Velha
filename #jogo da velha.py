tabuleiro = [[" ", " ", " "],
             [" "," "," "],
             [" "," "," "],
             ]
jogador = "X"
vencedor = False
rodadas = 0
while rodadas < 9 and vencedor == False:
    for linha in tabuleiro:
         print(" | ".join(linha))
         print("-" * 9)
    print(f"Vez do {jogador}")
    linha = int(input("Digite a linha (0, 1, 2) "))
    coluna = int(input("Digite a coluna (0, 1, 2)"))
    if linha >= 0 and linha <= 2 and coluna >= 0 and coluna <= 2:
     if tabuleiro[linha][coluna] == " ":
          tabuleiro[linha][coluna] = jogador
          rodadas += 1
          if tabuleiro[0][0] == jogador and tabuleiro[0][1] == jogador and tabuleiro[0][2] == jogador:
               vencedor = True
          if tabuleiro[1][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[1][2] == jogador:
             vencedor = True
          if tabuleiro[2][0] == jogador and tabuleiro[2][1] == jogador and tabuleiro[2][2] == jogador:
               vencedor = True
          if tabuleiro[0][0] == jogador and tabuleiro[1][0] == jogador and tabuleiro[2][0] == jogador:
                vencedor = True
          if tabuleiro[0][1] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][1] == jogador:
                vencedor = True
          if tabuleiro[0][2] == jogador and tabuleiro[1][2] == jogador and tabuleiro[2][2] == jogador:
                 vencedor = True
          if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
                 vencedor = True
          if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
                vencedor = True
          if vencedor == False:
            if jogador == "X":
                 jogador = "O"
            else:
                jogador = "X"
     else:
      print("Posição Ocupada")
    else:
        print("Digite um numero entre 0 e 2")
else:
     print("Digitou numeros fora do intervalo de 0 a 2")
for linha in tabuleiro:
    print(" | ".join(linha))
    print("-" * 9)

if vencedor == True:
    print("Jogador", jogador, "venceu!")
else:
    print("Empate!")