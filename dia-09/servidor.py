# Dia 9 — Servidor do Ragnarok — Lista de Dicionários

servidor = [
    {"nome": "Horio", "classe": "Novice", "hp": 100},
    {"nome": "Sacer", "classe": "Acolyte", "hp": 80},
    {"nome": "Mago", "classe": "Mage", "hp": 60}
]

# Adicionar novo jogador
servidor.append({"nome": "Guerreiro", "classe": "Swordman", "hp": 120})

# Mostrar todos os jogadores
print("=== Jogadores no Servidor ===")
for jogador in servidor:
    print(f"{jogador['nome']} | {jogador['classe']} | HP: {jogador['hp']}")

# Buscar jogador específico
print("\n=== Buscando jogador ===")
busca = "Sacer"
for jogador in servidor:
    if jogador["nome"] == busca:
        print(f"Encontrado: {jogador['nome']} | {jogador['classe']} | HP: {jogador['hp']}")