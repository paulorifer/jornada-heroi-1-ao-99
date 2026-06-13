import json
import os

def lista_compras():
    print("Lista de compras")
    item = input("Nome do item: ")
    quantidade = input("Quantidade: ")

    item_cadastro = {
        "item": item,
        "quantidade": quantidade
    }
    if os.path.exists("compras.json"):
        with open("compras.json", "r", encoding="utf-8") as arquivo:
            lista = json.load(arquivo)
    else:
        lista = []
    lista.append(item_cadastro)
    with open("compras.json", "w",  encoding="utf-8") as arquivo:
       json.dump(lista, arquivo, ensure_ascii=False, indent=4)

    print(f"\nItem salvo! Total na lista: {len(lista)} item(s).")

lista_compras()