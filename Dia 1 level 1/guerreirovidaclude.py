nome = "Guerreiro"
hp = 80
pocaohp = 30


dano1 = 35
hp = hp - dano1
print(f"{nome} tomou {dano1} de dano. HP restante: {hp}")

hp = hp + pocaohp
print (f"{nome} tomou {pocaohp} e se curou!") 

dano2 = 60
hp = hp - dano2
print(f"{nome} tomou {dano2} de dano. HP restante: {hp}")

if hp <= 0:
    print(f"{nome} morreu!!")

       
else:
    print(f"{nome} sobreviveu com {hp} de HP!")
