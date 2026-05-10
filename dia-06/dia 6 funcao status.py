## Cria uma função chamada status que recebe nome e hp.##
## Se o HP for maior que 50 → "está saudável"##
# Se for entre 20 e 50 → "está ferido"###
# Se for menor que 20 → "está em perigo!" ##


def status(nome, hp):
    if hp > 50:
        print("esta saudavel")
    elif hp > 20 and hp <= 50:
        print("esta ferido")
    elif hp < 20:
        print("está em perigo")


status("nome", 60)
status("Guerreiro", 35)
status("Mago", 10)