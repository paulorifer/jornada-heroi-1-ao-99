nome = "Dragao"
drahp = 150
guerreiro_espada = 30

for i in range(6):
    drahp = drahp - guerreiro_espada
    print(f"Ataque {i+1} Dragao ficou com {drahp} de Hp")
    if drahp <=0:
        print("dragao morreu. Vitoria")
        break
if drahp >= 0:
    print(f"{nome} sobreviveu!")
        
else:
    print(f"{nome} não resistiu e não sobreviveu!")

