import json
import os

ARQUIVO = "produtos.json"

def carregar():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
             return json.load(f)
    return[]
def salvar (lista):
    with open(ARQUIVO, "w") as f:
        json.dump(lista, f) 
produtos = carregar()
produtos.append({"nome": "Notbook", "preco": 3500})
salvar (produtos)
print(produtos)          