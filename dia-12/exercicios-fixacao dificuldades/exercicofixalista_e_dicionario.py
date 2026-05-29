##Cria uma lista chamada pedidos com 3 dicionários. Cada dicionário tem: cliente, produto e quantidade. Depois:
#Imprime o produto do segundo pedido
#Imprime o cliente do terceiro pedido
#Percorre todos e imprime: "Cliente: X — Produto: Y — Quantidade: Z"
pedidos = [
    {"nome": "Paulo", "produto": "cimento", "quant": 10},
    {"nome": "Ana", "produto": "Argamassa AcIII Flex", "quant": 20},
    {"nome": "Edvan", "produto": "Piso Porcelanato 60x60", "quant": 7}
]
print(pedidos[1]["produto"])
print(pedidos[2]["nome"])
for pedido in pedidos:
   print("Cliente:", pedido["nome"], "— Produto:", pedido["produto"], "— Quantidade:", pedido["quant"])


   ##for pedido in pedidos:
   # print(f"Cliente: {pedido['nome']} — Produto: {pedido['produto']} — Quantidade: {pedido['quant']}")##
   #pode usar assim também é a mesma coisa mais facil , acostumar a usar os dois tipos