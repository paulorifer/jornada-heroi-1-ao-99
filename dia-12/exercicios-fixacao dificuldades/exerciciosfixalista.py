##lista##
##xercício 1 — Cria uma lista chamada clientes com 3 nomes. Depois:
##
##Imprime o segundo cliente
##Adiciona um quarto cliente
##Imprime quantos clientes tem no total
##Percorre a lista e imprime todos ##


clientes = ["João", "Carmem", "Felipe"]

print(clientes[0])
print(clientes[1])
print(clientes[2])

clientes.append("Ana")

print(len(clientes))

for cliente in clientes:
    print(cliente)

    ##ficar atendo sempre o mesmo nome no for ex: cliente = cliente (print) (nao esquecer)