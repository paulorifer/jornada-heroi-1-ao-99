import json
import os

def cadastrar_produto():
    print("=== CADASTRO DE PRODUTO ===")
    codigo_rp = input("Codigo RP: ")
    loja = input("Numero da Loja: ")
    produto = input("Nome do Produto: ")
    cliente = input("Nome do Cliente: ")
    cpf = input("CPF do Cliente: ")
    localizacao = input("Localizacao fisica (Ex: Galpão A, Prateleira 4 Prox: Cimento): ")

    produto_cadastrado = {
        "codigo_rp": codigo_rp,
        "loja": loja,
        "produto": produto,
        "cliente": cliente,
        "cpf": cpf,
        "localizacao": localizacao,
        "retirado": False
    }
    if os.path.exists("estoque.json"):
        with open("estoque.json", "r", encoding="utf-8") as arquivo:
            estoque = json.load(arquivo)
    else:
        estoque = []

    estoque.append(produto_cadastrado)

    with open("estoque.json", "w", encoding="utf-8") as arquivo:
        json.dump(estoque, arquivo, ensure_ascii=False, indent=4)

    print(f"\nProduto salvo! Total no estoque: {len(estoque)} produto(s).")


cadastrar_produto()