nome = "lobo"
hplobo = 60
adagalad = 25

for i in range(4):
    hplobo = hplobo - adagalad
    print(f"Ataque {i+1}! Lobo ficou com {hplobo} de HP")
if hplobo >0:
    print(f"{nome} sobreviveu!")
else:
    print (f"{nome} não resisitu e não sobreviiveu!")
           


## Exercicio fixação 2###

nome = "Dragao"
drahp = 150
guerreiro_espada = 30

for i in range(6):
    drahp = drahp - guerreiro_espada
    print(f"Ataque {i+1} Dragao ficou com {drahp} de Hp")
if drahp >0:
    print (f"{nome} sobreviveu!")
else:
    print (f"{nome} não resistiu e não sobreviveu!")        

