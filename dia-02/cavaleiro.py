nome = "cavaleiro"
hp_cav = 100
ataque_espada = 40
ataque_cav = ataque_espada*3
dragao_hp = 200
inimigo = "dragao"
dano_fogo = 80
hp_cav = 100 - dano_fogo
dragao_hp = 200 - ataque_cav



print (f"{nome} atacou e deu {ataque_cav} de dano no {inimigo}!!")

ataque_drag = dano_fogo
print (f"{inimigo} contra adacou o {nome} e deu de dano {ataque_drag}!!")

if hp_cav >0:
    print ("Cavaleiro resistiu ao ataque e sobrevivieu!!")
else: 
    print ("Cavaleiro nao resisitu e não sobrevivieu")

if dragao_hp >0:
    print ("Dragão é forte e sobrevivieu!!")
else:
    print ("Dragão foi derrotado!!")