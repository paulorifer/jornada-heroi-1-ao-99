def curar(sacer, hp, curahp):
    curahp = hp + curahp 
    print(f"{sacer} usou cura! Curou {curahp}")
    if hp <=10:
        print(f"{sacer} recuperou hp {curahp}")
    elif hp >=10:
        print(f"{sacer} não precisa usar skill de curar")

curar("sacer", 5, 30)
