nome = "lobo"
adagalad = 25
hplobo = 60

ataqlobo = hplobo - adagalad * 2


if ataqlobo >= 0:
    print(f"{nome} Sofreu ataque . Resta de vida {ataqlobo}")
else:
    print(f"{nome} Sofreu a ataque e não resistiu {ataqlobo}")
