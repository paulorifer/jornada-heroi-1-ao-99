def escudo(sacer, dano):
    dano_real = dano - 15
    print(f"{sacer} usou escudo! Dano real: {dano_real}")
    if dano_real >30:
        print("Dano alto o escudo não foi suficiente!")
    elif dano_real <=30:
         print("Escudo segurou bem o ataque!")       
escudo("sacer", 40)