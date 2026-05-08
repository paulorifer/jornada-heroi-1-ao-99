

nome = "mago"
nomeinimigo = "orc"
hp = 60
mana = 100
magia = 40
danomagico = 50

inimigohp = 80

mana = mana - magia
print(f"{nome} Usou magia!  Mana restante: {mana}")

inimigohp = inimigohp - danomagico
print(f"{nomeinimigo} tomou {danomagico}dano")

if inimigohp > 0:
    print(f"{nome} sobreviveu  com {inimigohp} de HP!")
else:
    print(f"{nome} morreu!")
