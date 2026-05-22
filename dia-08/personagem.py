# Dia 8 — Ficha do Personagem com Dicionário

personagem = {
    "nome": "Horio",
    "classe": "Novice",
    "nivel": 8,
    "hp": 100,
    "sp": 60
}

# Alterar HP após dano
personagem["hp"] = 50

# Mostrar ficha completa
print("=== Ficha do Personagem ===")
for chave, valor in personagem.items():
    print(f"{chave}: {valor}")

print(f"\nTotal de atributos: {len(personagem)}")