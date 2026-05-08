nome = "arqueiro"
inimigo = "goblin"
hp = 70
flechas = 50
inimigohp = 60
flechadano = 15
atiraflecha = 3
vida_inimigo = inimigohp - flechadano*atiraflecha

flechas_rest = 50 - 3
print(f"{nome} fez seu ataque de flechas . Restou {flechas_rest} de flechas")

if vida_inimigo >= 0:
    print(f"{inimigo} sofreu ataque!. Restou {vida_inimigo} de HP! Ele sobreviveu")
else:
    print(f"{inimigo}Inimigo morreu")
