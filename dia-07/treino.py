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


###    #####

itens = ["capa", "sobrepeliz", "sapato", "brinco"]

def mostrar_inventario(itens):
    for i, item in enumerate(itens):
        print(f"Slot {i}: {item}")
    print(f"\nTotal de itens: {len(itens)}")

mostrar_inventario(itens)