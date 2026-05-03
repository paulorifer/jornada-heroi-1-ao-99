## Jornada do heroi dia 1 programação inicial ##


vida = int(input("Digite a vida do personagem: "))
ataque_inimigo = int(input("Digite o dano do inimigo: "))

vida = vida - ataque_inimigo

if vida <= 0:
    print("Personagem morreu")
elif vida < 50:
    print("Usar poção")
else:
    print("Continuar lutando")

   ### # Próximo passo: usar input() para digitar os valores##
