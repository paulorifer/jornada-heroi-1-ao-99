#Cria um arquivo novo chamado fixajson.py com:

#import json e import os
#Constante ARQUIVO = "fixa.json"
#Função carregar_dados() — carrega o arquivo se existir, senão retorna lista vazia
#Função salvar_dados(lista) — salva a lista no arquivo
#Cria uma lista com 2 dicionários — cada um com nome e valor
#Salva a lista com salvar_dados()
#Carrega de volta com carregar_dados() e imprime##


import json
import os

ARQUIVO = "fixa.json"

def carregar_dados():
    if os.path.exists(ARQUIVO):
        with open (ARQUIVO, "r") as f:
            return json.load(f)
    return[]

def salvar_dados(lista):
    with open(ARQUIVO, "w") as f:
        json.dump(lista, f)
dados = [
    {"nome": "cimento", "valor": 35},
    {"nome": "Areia media", "valor": 28}
]
salvar_dados(dados)

resultado = carregar_dados()
print(resultado)