def atacar (nome_inimigo, hp_inimigo , dano):
    print(f"atacando {nome_inimigo}")
    for i in range(3):
        hp_inimigo = hp_inimigo - dano
        print(f"ataque {i+1}! {nome_inimigo} esta com {hp_inimigo} de HP")
    if hp_inimigo <= 0:
        print(f"{nome_inimigo} foi derrotado!")
    else:
        print(f"{nome_inimigo} sobreviveu com {hp_inimigo} de HP")        

atacar("Lobo", 60, 25)           
atacar("Dragão", 150, 30)
atacar("Goblin", 40, 25)