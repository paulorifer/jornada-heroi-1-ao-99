## Cria uma função chamada status que recebe nome e hp.##
## Se o HP for maior que 50 → "está saudável"##
# Se for entre 20 e 50 → "está ferido"###
# Se for menor que 20 → "está em perigo!" ##


def status(nome, hp):
    if hp > 50:
        print(f"{nome} esta saudavel")
    elif hp > 20 and hp <= 50:
        print(f"{nome} esta ferido")
    elif hp < 20:
        print(f"{nome} está em perigo")


status("horio", 60)
status("Guerreiro", 35)
status("Mago", 10)