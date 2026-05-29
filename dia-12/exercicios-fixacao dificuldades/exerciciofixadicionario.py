##Cria um dicionário chamado funcionario com as chaves: nome, cargo e salario. Depois:

#Imprime só o cargo
#Muda o salário para um valor maior
#Adiciona a chave setor com um valor
#Percorre e imprime todas as chaves e valores


funcionario = {"nome": "Paulo", "cargo": "Logística", "salario": 1800}

print(funcionario["cargo"])

funcionario["salario"] = 2188
print(funcionario["salario"])

funcionario["setor"] = "Logistico"

for chave, valor in funcionario.items():
    print(chave, ":", valor)

    ##lembrete: dicionario["chave"] = valor   sem espaço, sem = dentro do colchete