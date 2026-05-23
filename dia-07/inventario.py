# Dia 7 — Sistema de Inventário do Horio

inventario = ["Espada Coreana", "Poção Vermelha", "Chapéu de Coelho"]

inventario.append("Anel de Maestro")
inventario.remove("Poção Vermelha")

print("=== Inventário do Horio ===")
for i, item in enumerate(inventario):
    print(f"Slot {i}: {item}")

print(f"\nTotal de itens: {len(inventario)}")