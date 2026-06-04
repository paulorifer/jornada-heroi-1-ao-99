funcionarios = [

    {"nome": "Ana", "setor": "TI", "salario": 3200 },
    {"nome": "Bruno", "setor": "Logistica", "salario": 2800},
    {"nome" : "Otavio", "setor": "Administrativo", "salario": 7250},
]    

print(funcionarios[1]["nome"])
print (funcionarios[2]["salario"])
for f in funcionarios:
    if f["setor"] == "TI":
        print(f["nome"])
        