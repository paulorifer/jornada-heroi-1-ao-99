import json

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

    with open("estoque.json", "w", encoding="utf-8") as arquivo:
        json.dump(produto_cadastrado, arquivo, ensure_ascii=False)

    print("\nProduto salvo com sucesso!")

cadastrar_produto()