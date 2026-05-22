hp = 15
if hp <20:
    print("Horio esta em perigo!")
else:
    print("Horio esta saudavel!")    

##  ###

inventario = ["cajado", "botas", "sobrepeliz"]
inventario.append("brincos")

for i, item in enumerate(inventario):
    print(f"Slot {i}: {item}")

print(f"\nTotal de equipamentos: {len(inventario)}")
