import json


estoque = [
{"nome" : "cimento", "quantidade": 70, "categoria": "construção"},
{"nome" : "Argamassa", "quantidade": 197, "categoria": "construção"},
{"nome" : "Piso Formigues", "quantidade": 23, "categoria": "construção"}
]


with open("estoque.json", "w", encoding="utf-8") as arquivo:
    json.dump(estoque, arquivo, ensure_ascii=False)
with open("estoque.json", "r", encoding="utf-8") as arquivo:
    estoque_carregado = json.load(arquivo)
print(estoque_carregado)