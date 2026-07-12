import json
import os
from datetime import datetime

def buscar_produto():
    print("= Busca de Produto = ")
    cpf = input("Digite o CPF do Cliente: ")
    if os.path.exists("estoque.json"):
        with open("estoque.json", "r", encoding="utf-8") as arquivo:
            estoque = json.load(arquivo)
    else:
        estoque = []
    for produto in estoque:
        if produto["cpf"] == cpf:
            print("Produto encontrado!")
            print(f"Cliente: {produto['cliente']}")
            print(f"CPF: {produto['cpf']}")
            print(f"Produto: {produto['produto']}")
            print(f"Localização: {produto['localizacao']}")
            print(f"Pedido nº: {produto['numero_pedido']}")
            print(f"Nota fiscal: {produto['nota_fiscal']}")
            print(f"Data de chegada: {produto['data_chegada']}")
            print(f"Retirado: {produto['retirado']}")

def marcar_retirado():
    print("=== MARCAR COMO RETIRADO ===")
    cpf = input("Digite o CPF do Cliente: ")
    if os.path.exists("estoque.json"):
        with open("estoque.json", "r", encoding="utf-8") as arquivo:
            estoque = json.load(arquivo)
    else:
        estoque = []
    for produto in estoque:
        if produto["cpf"] == cpf:
            produto["retirado"] = True
            print(f"Produto '{produto['produto']}' marcado como retirado!")
    with open("estoque.json", "w", encoding="utf-8") as arquivo:
        json.dump(estoque, arquivo, ensure_ascii=True, indent=4)            

def cadastrar_produto():
    print("=== CADASTRO DE PRODUTO ===")
    codigo_rp = input("Codigo RP: ")
    loja = input("Numero da Loja: ")
    produto = input("Nome do Produto: ")
    cliente = input("Nome do Cliente: ")
    cpf = input("CPF do Cliente: ")
    localizacao = input("Localizacao fisica (Ex: Galpão A, Prateleira 4 Prox: Cimento): ")
    numero_pedido = input("Numero do Pedido: ")
    nota_fiscal = input("Nota fiscal do fornecedor: ")
    data_chegada = datetime.now().strftime("%d/%m/%Y %H:%M")
    produto_cadastrado = {
        "codigo_rp": codigo_rp,
        "loja": loja,
        "produto": produto,
        "cliente": cliente,
        "cpf": cpf,
        "localizacao": localizacao,
        "numero_pedido": numero_pedido,
        "nota_fiscal": nota_fiscal,
        "data_chegada": data_chegada,
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

while True:
    print("== CONIBASE ==")
    print("1 - Cadastrar Produto")
    print("2 - Buscar Produto")
    print("3 - Marcar como Retirado")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        cadastrar_produto()
    elif opcao == "2":
        buscar_produto()
    elif opcao == "3":
        marcar_retirado()
    elif opcao == "0":
        print("Encerrando o sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")