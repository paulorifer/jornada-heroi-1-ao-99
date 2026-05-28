#Sistema de Estoque  - Conibase
# Dia 10 - Jornada Python - Paulo

estoque = [
    {"nome": "Porcelanato Acetinado", "quantidade": 50, "preco": 89.90},
    {"nome": "Argamassa AC-ll", "quantidade": 30, "preco": 25.50},
    {"nome": "Rejunte branco", "quantidade": 100, "preco": 12.00},
]

def listar_produtos():
    print("\n====ESTOQUE ATUAL====")
    for i, produto in  enumerate(estoque):
        print(f"{i+1}. {produto['nome']} | Qtd: {produto['quantidade']} | R$ {produto['preco']:.2f}")
    print("=============================")              
listar_produtos() 
def buscar_produto(nome_busca):
    print(f"\nBuscando por  '{nome_busca}'....")
    for produto  in estoque:
        if nome_busca.lower() in produto ["nome"].lower():
            print(f"Encontrado: {produto['nome']} | Qtd: {produto['quantidade']} | R$ {produto['preco']:.2f}")
            return
    print("  Produto não encontrado.")
    print("=============================")              
buscar_produto("argamassa")
def adicionar_produto(nome, quantidade, preco):
    novo = {"nome": nome, "quantidade": quantidade, "preco": preco}
    estoque.append(novo)
    print(f"\nProduto '{nome}' adicionado com sucesso!")
adicionar_produto("Cimento CP-II", 80, 35.00)
listar_produtos()        
def atualizar_quantidade(nome_busca, nova_quantidade):
    for produto in estoque:
        if nome_busca.lower() in produto["nome"].lower():
            produto["quantidade"] = nova_quantidade
            print(f"\nQuantidade de '{produto['nome']}' atualizada para {nova_quantidade}!")
            return
    print("Produto não encontrado.")
listar_produtos()
atualizar_quantidade("rejunte", 200)
listar_produtos()    
def remover_produto(nome_busca):
    for produto in estoque:
        if nome_busca.lower() in produto["nome"].lower():
            estoque.remove(produto)
            print(f"\nProduto '{produto['nome']}' removido do estoque!")
            return
    print("Produto não encontrado.")
listar_produtos()
remover_produto("cimento")
listar_produtos()    


